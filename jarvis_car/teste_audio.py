import pyaudio
import struct

pa = pyaudio.PyAudio()

stream = pa.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=16000,
    input=True,
    frames_per_buffer=1024
)

print("Fale algo...")

while True:
    data = stream.read(1024, exception_on_overflow=False)
    volume = max(struct.unpack("1024h", data))
    print(volume)
