import os

from gtts import gTTS
import playsound    
import pyttsx3


def NikkiSay(text):
    try:
        t = gTTS(text=text, lang='en')
        fileName = "voice.mp3"
        t.save(fileName)
        playsound.playsound(fileName)
    except Exception as e:
        eng = pyttsx3.init()
        voices = eng.getProperty('voices')
        eng.say(text)
        eng.runAndWait()
# create the list with the random numbers with integer
