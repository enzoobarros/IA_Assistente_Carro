import pyaudio
import numpy as np
from openwakeword.model import Model
import time

print("Iniciando Jarvis (WakeWord)...")

model = Model(
    wakeword_models=["hey_jarvis"],
    inference_framework="onnx"
)

pa = pyaudio.PyAudio()

# ⚠️ Se quiser, depois podemos forçar o índice
MIC_INDEX = None  

stream = pa.open(
    rate=16000,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=1280,
    input_device_index=MIC_INDEX
)

print("🎧 Ouvindo... diga 'HEY JARVIS'")

# pequeno aquecimento
time.sleep(1)

while True:
    data = stream.read(1280, exception_on_overflow=False)
    audio = np.frombuffer(data, dtype=np.int16)

    prediction = model.predict(audio)
    score = prediction["hey_jarvis"]

    # DEBUG VISUAL
    print(f"score: {score:.2f}", end="\r")

    if score > 0.25:
        print("\n🟢 Jarvis ativado!")
        time.sleep(1)
