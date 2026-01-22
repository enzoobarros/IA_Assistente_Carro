print("INICIO DO SCRIPT")

import pvporcupine
import pyaudio
import struct

# ⬇️ COLOQUE AQUI O ID DO MICROFONE
MIC_INDEX = 1  # ex: 1

porcupine = pvporcupine.create(keywords=["jarvis"])
pa = pyaudio.PyAudio()

stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length,
    input_device_index=MIC_INDEX
)

print("🎧 Ouvindo... diga 'Jarvis'")

try:
    while True:
        pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        if porcupine.process(pcm) >= 0:
            print("🟢 Jarvis ativado!")
except KeyboardInterrupt:
    print("Encerrando...")
finally:
    stream.stop_stream()
    stream.close()
    pa.terminate()
