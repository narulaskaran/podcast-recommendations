import speech_recognition as sr
import audioread as au
import math

NUM_CHUNKS = 10
CHUNKS = [None for i in range(NUM_CHUNKS - 1)]
# FILEPATH = "./audio/harvard.wav"
FILEPATH = "./audio/Freakonomics_Zoom_Doctors.wav"
LENGTH = -1

with au.audio_open(FILEPATH) as f:
    LENGTH = f.duration

print("Transcribing: ", FILEPATH)
print("Duration: ", LENGTH)

r = sr.Recognizer()
audioFile = sr.AudioFile(FILEPATH)
with audioFile as source:
    for i in range(len(CHUNKS)):
        CHUNKS[i] = r.record(source, duration= math.ceil(LENGTH / NUM_CHUNKS))
        print("-- Recorded chunk {} --".format(i))

for chunk in CHUNKS:
    if chunk != None:
        print(r.recognize_google(chunk))
        print("-- Transcribed chunk {} --".format(i))