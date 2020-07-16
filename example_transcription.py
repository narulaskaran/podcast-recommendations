import numpy as np
import speech_recognition as sr

print("hello, world!")

r = sr.Recognizer()
harvard = sr.AudioFile("./audio/harvard.wav")
with harvard as source:
    audio = r.record(source)

print(r.recognize_google(audio))