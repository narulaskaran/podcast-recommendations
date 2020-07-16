import speech_recognition as sr
import audioread as au
import math

NUM_CHUNKS = 10
CHUNKS = [None for i in range(NUM_CHUNKS)]
# FILEPATH = "./audio/JRE_Bernie_Sanders.wav"
FILEPATH = "./audio/harvard.wav"
LENGTH = -1

with au.audio_open('./audio/harvard.wav') as f:
    LENGTH = f.duration

print("Transcribing: ", FILEPATH)
print("Duration: ", LENGTH)

r = sr.Recognizer()
audioFile = sr.AudioFile(FILEPATH)
with audioFile as source:
    for i in range(NUM_CHUNKS - 1):
        CHUNKS[i] = r.record(source, duration= math.ceil(LENGTH / NUM_CHUNKS))

for chunk in CHUNKS:
    if chunk != None:
        print(r.recognize_google(chunk))