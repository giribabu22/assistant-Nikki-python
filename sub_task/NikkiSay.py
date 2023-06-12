import os

try:
    from gtts import gTTS
    import playsound    
    import pyttsx3

except ImportError:
    os.system('sudo apt-get install python3-tk python3-dev')
    os.system('sudo apt install espeak')
    os.system('sudo apt-get install libxml2 libxml2-dev libxslt1-dev')
    os.system('pip install lxml')
    os.system('sudo apt-get install portaudio19-dev')
    os.system('pip install selenium')
    os.system('pip install playsound')
    os.system('pip install gtts')
    os.system('pip install pyaudio')
    os.system('pip install pyttsx3')

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
