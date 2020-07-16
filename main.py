import numpy as np
import sklearn
import speech_recognition as sr

print("hello, world!")

r = sr.Recognizer()
harvard = sr.AudioFile("./harvard.wav")
with harvard as source:
    audio = r.record(source)