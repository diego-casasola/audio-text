import os

import pyaudio
import wave
from pydub import AudioSegment

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Grabando...")

frames = []
seconds = 2
for i in range(0, int(RATE / CHUNK * seconds)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Grabacion terminada")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open("output.wav", "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b"".join(frames))
wf.close()

wav_audio = AudioSegment.from_wav("output.wav")

wav_audio.export('mp3/', format="mp3")

# import whisper
#
# model = whisper.load_model("base")
# result = model.transcribe("output.wav")
# print(result["text"])