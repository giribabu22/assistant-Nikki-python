import asyncio
import threading
import time
import speech_recognition as sr

r = sr.Recognizer()

# def do(audio):


def srcVoice(n, audio):
    for i in range(n, 0, -1):
        print('sssssss')
        # threading.Thread(target=r.recognize_google, args=(audio))
        words = r.recognize_google(audio)
        print(words, '$$$$$$$$$$$$')
        break

def audioLis(source):
    print('running')
    try:
        audio = r.listen(source, 3, 6)
        try:
            DN = threading.Thread(target=srcVoice, args=(1, audio))
            DN.start()
        except Exception as e:pass
    except Exception as e:

        print(e, '<<<<<<<<<<<<<<<<<<<')
source = 'None'
with sr.Microphone() as source:
    while True:
        audioLis(source)
        
# async
# await
