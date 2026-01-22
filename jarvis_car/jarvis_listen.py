import pyaudio
import numpy as np
import time
import asyncio
import os
import pygame
import edge_tts
import datetime

from jarvis_brain import perguntar_jarvis
from openwakeword.model import Model
from faster_whisper import WhisperModel


# ======================
# INIT
# ======================
pygame.mixer.init()
print("Iniciando JARVIS completo...")


# ======================
# CONTROLE DE ESTADO
# ======================
jarvis_falando = False
cooldown = False
last_trigger = 0


# ======================
# TTS (EDGE)
# ======================
VOICE = "pt-BR-AntonioNeural"

async def falar_async(texto):
    global jarvis_falando

    if not texto.strip():
        return

    jarvis_falando = True
    arquivo = "fala.mp3"

    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

        communicate = edge_tts.Communicate(
            texto,
            VOICE,
            rate="+5%",
            volume="+0%"
        )

        await communicate.save(arquivo)

        pygame.mixer.music.load(arquivo)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            await asyncio.sleep(0.05)

    except Exception as e:
        print("❌ Erro no TTS:", e)

    finally:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        jarvis_falando = False


def falar(texto):
    asyncio.run(falar_async(texto))


# ======================
# FUNÇÕES ÚTEIS
# ======================
def hora_atual():
    agora = datetime.datetime.now()
    return f"Agora são {agora.hour} horas e {agora.minute} minutos."


# ======================
# PROCESSAMENTO
# ======================
def processar_comando(texto):
    texto = texto.lower().strip()
    print("🗣️ Você disse:", texto)

    # ⏰ HORAS
    if "que horas" in texto or "horário" in texto:
        resposta = hora_atual()
        print("🤖 Jarvis:", resposta)
        falar(resposta)
        return

    # 🤖 IA
    try:
        resposta = perguntar_jarvis(texto)

        if not resposta:
            resposta = "Desculpe, não entendi."

        print("🤖 Jarvis:", resposta)
        falar(resposta)

    except Exception as e:
        print("❌ Erro na IA:", e)
        falar("Ocorreu um erro ao processar sua solicitação.")


# ======================
# WAKE WORD
# ======================
wake_model = Model(
    wakeword_models=["hey_jarvis"],
    inference_framework="onnx"
)


# ======================
# WHISPER
# ======================
whisper = WhisperModel("base", compute_type="int8")


# ======================
# ÁUDIO
# ======================
pa = pyaudio.PyAudio()

stream = pa.open(
    rate=16000,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=1280
)

print("🎧 Aguardando 'HEY JARVIS'...\n")


# ======================
# LOOP PRINCIPAL
# ======================
while True:

    if jarvis_falando:
        time.sleep(0.02)
        continue

    data = stream.read(1280, exception_on_overflow=False)
    audio = np.frombuffer(data, dtype=np.int16)

    prediction = wake_model.predict(audio)
    score = prediction["hey_jarvis"]

    if score > 0.4 and not cooldown:
        print("🟢 Jarvis ativado! Fale agora...")
        last_trigger = time.time()
        cooldown = True

        frames = []
        for _ in range(50):
            frames.append(stream.read(1280, exception_on_overflow=False))

        audio_np = (
            np.frombuffer(b"".join(frames), dtype=np.int16)
            .astype(np.float32) / 32768.0
        )

        segments, _ = whisper.transcribe(audio_np, language="pt")

        texto = " ".join(seg.text.strip() for seg in segments).strip()

        if texto:
            processar_comando(texto)

    if cooldown and time.time() - last_trigger > 3:
        cooldown = False
        print("🎧 Aguardando 'HEY JARVIS'...")
