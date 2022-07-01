'''
this is my personal assistant name is Nikki 
    if you want to use it 
    there is some rule
    1) if you want time or weather you need to say 'Nikki time in city name or country name' Ex : Nikki time in india 
                                                    Nikki weather in city name or country name  Ex Nikki  weather in Russia
    2) if you want any person,company,ngo and anything,you need to say 'who is person name' Ex : who is ram  
    3) if you want ask Nikki personal questions you can like how are you, what about you,Nikki what are you doing
    4) if you want to search any to more you need to say 'Nikki search' and what you want to search Ex : Nikki search 2+2 how much
    and it will open your browser and it will search for you , 
    5) if you say Nikki open instagram  it will open the browser and it will open instagram for you 
    ^ this is my total python learning skills  
    '''

# i used some modules in this projects like selenium,pyttsx3,speech recognition, Beautifulsoup,and some others

import time
from distutils.log import error
from gettext import find
from subprocess import call
import speech_recognition as sr
import requests,random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup as useMe
import pyttsx3

joke_nik = [['I invented a new word!Plagiarism!],[Did you hear about the mathematician who’s afraid of negative numbers?He’ll stop at nothing to avoid them.'],['Why do we tell actors to “break a leg?”Because every play has a cast. Here are some dark jokes to check out if you have a morbid sense of humor.'],['Helvetica and Times New Roman walk into a bar.“Get out of here!” shouts the bartender. “We don’t serve your type.”],[Yesterday I saw a guy spill all his Scrabble letters on the road. I asked him, “What’s the word on the street?”Once my dog ate all the Scrabble tiles. For days he kept leaving little messages around the house. Don’t miss these hilarious egg puns that will absolutely crack you up.'],['Knock! Knock! Who’s there? Control Freak. Con… OK, now you say, “Control Freak who?”' ],['Hear about the new restaurant called Karma? There’s no menu: You get what you deserve.'],['A woman in labor suddenly shouted, “Shouldn’t! Wouldn’t! Couldn’t! Didn’t! Can’t!”“Don’t worry,” said the doc. “Those are just contractions.”'],['A bear walks into a bar and says, “Give me a whiskey and … cola.” “Why the big pause?” asks the bartender. The bear shrugged. “I’m not sure; I was born with them.”'],['Did you hear about the actor who fell through the floorboards?He was just going through a stage.'],['Did you hear about the claustrophobic astronaut? He just needed a little space.'],['Why don’t scientists trust atoms? Because they make up everything.'],['Why did the chicken go to the séance?To get to the other side. Check out these other “why did the chicken cross the road?” jokes for more laughs.'],['Where are average things manufactured?The satisfactory.'],['How do you drown a hipster? Throw him in the mainstream.'],['What sits at the bottom of the sea and twitches?A nervous wreck.'],['What does a nosy pepper do? Gets jalapeño business!'],['How does Moses make tea? He brews.'],['Why can’t you explain puns to kleptomaniacs?They always take things literally.'],['How do you keep a bagel from getting away?Put lox on it.'],['A man tells his doctor, “Doc, help me. I’m addicted to Twitter!”The doctor replies, “Sorry, I don’t follow you …”']]

eng = pyttsx3.init()
voices = eng.getProperty('voices')
eng.setProperty('voice', 'english_rp+f2') 
eng.runAndWait()
eng.setProperty('volume', 4.0)


def NikkiVoiceSource():
    r = sr.Recognizer()                                                       
    with sr.Microphone() as source:                                                  
        print("Listening… :")  
        eng.say('Listening…')
        eng.runAndWait()                         
        audio = r.listen(source)  
    return r.recognize_google(audio)

def NikkiPlaySong():
  driver = webdriver.Firefox(executable_path="/home/navgurukul/Downloads/geckodriver-v0.31.0-linux64/geckodriver")
  driver.get('https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F')
  input_user = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Email address or username']")))
  input_user.send_keys('giribabu22@navgurukul.org') 
  input_pin = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Password']")))
  input_pin.send_keys('prem@123')
  sub = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[id='login-button']"))).click()     

def NikkiYoutube(song):
  print(song)
  song = song.replace(' ','+')
  driver = webdriver.Firefox(executable_path="/home/navgurukul/Downloads/geckodriver-v0.31.0-linux64/geckodriver")
  driver.get(f'https://www.youtube.com/results?search_query={song}')
  src2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))
  src2.send_keys(song) 
  time.sleep(2)
  src2.send_keys(Keys.ENTER)

def NikkiBoring():
    while True:
        try:
            eng.say("what about you Boss :")
            eng.runAndWait()
            myans = NikkiVoiceSource()
            if 'boring' in myans:
                eng.say('if you want i will play something on youtube and jokes for you ')
                eng.runAndWait()
                ply = NikkiVoiceSource()
                print('you say :',ply)
                list_play = ['telugu songs','ellie goulding','chaganti koteswara rao speeches mahabharatham etv','SriGarikipatiNarasimhaRaoOfficial','summer ball 2022']
                cho = random.choice(list_play)
                if 'YouTube' in ply:
                    NikkiYoutube(cho)
                    break
                elif 'joke' in ply :
                    NikkiNewstoday()
                    break
                elif 'you play' in ply:
                    res = ply.find('you play')+8
                    NikkiYoutube(ply[res:])

            elif 'fine' in myans:
                eng.say('great to hear from you')
                eng.runAndWait()
                break
            else:
                eng.say('hohoho i dont what you mean !!')
                eng.runAndWait()
        except sr.UnknownValueError:
            print('Could not understand audio')
            eng.say('Could not understand audio')
            eng.runAndWait()
            pass

def timeFun():
  t = NikkiTime('india')
  if t >= 1 and t <= 12 :
      res = 'good morning'
  elif t >= 13 and t <= 15:
      res = 'good afternoon'
  elif t >= 16 and t <= 20:
      res = 'good evening'
  else :
      res = 'good night'
  eng.say(f'Hello Boss {res}')
  eng.runAndWait()

def NikkiWhoIs(user_audio_text):                                         # this function help, to find the who is questions
  last_url = str(user_audio_text).replace(' ','+')
  url = 'https://www.google.com/search?q='+last_url
  page = requests.get(url).text
  soup = useMe(page,'lxml')
  data =soup.prettify()
  r = soup.find('div' ,class_="kCrYT").getText()
  print(r)
  eng.say(r)
  eng.runAndWait()

def NikkiWork():
    f = open('/home/navgurukul/Desktop/workOftheday.txt')
    res = f.read()
    eng.say(res)
    eng.runAndWait()

def NikkiInsta(username,password):                                     # this function do , auto login instagram            
  driver = webdriver.Firefox(executable_path="/home/navgurukul/Downloads/geckodriver-v0.31.0-linux64/geckodriver")
  driver.get('https://www.instagram.com/accounts/login/')
  user_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
  user_name.clear()
  user_name.send_keys(username)
  pas = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name = 'password']")))
  pas.clear()
  pas.send_keys(password)
  log_in = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type = 'submit']"))).click()  
  time.sleep(2)
  not_now2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()
  not_now3 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()

  searchbox = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))

  searchbox.clear()
  searchbox.clear()
  keyword = 'click_theworld1'
  searchbox.send_keys(keyword)
  time.sleep(2)
  searchbox.send_keys(Keys.ENTER)
  time.sleep(2)
  searchbox.send_keys(Keys.ENTER)

def NikkiTime(timeL):                                    # this function tell time 
  url = f'https://www.google.com/search?q=time+{timeL}'
  page = requests.get(url).content
  soup = useMe(page,'lxml')
  data = soup.find('div',class_="BNeawe iBp4i AP7Wnd")
  print(data.text)
  eng.say(data.text)
  eng.runAndWait()
  return int(data.text[:-6])


def NikkiNewstoday():
  latestNews = []
  url = 'https://www.ndtv.com/latest'
  page = requests.get(url).text
  soup = useMe(page,'lxml')
  d = soup.findAll('div',class_="news_Itm")
  r = random.randrange(0,len(d)-1)
  for i in d:
      latestNews.append(i.text)
  if latestNews[r] in 'window._taboola ':
      del latestNews[r]
  print('this is : ',latestNews[r])
  eng.say(latestNews[r])
  eng.runAndWait()

def NikkiSearch():                                         # this function search anything in the browser
  driver = webdriver.Firefox(executable_path="/home/navgurukul/Downloads/geckodriver-v0.31.0-linux64/geckodriver")
  driver.get('https://www.google.com/')
  src = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='q']")))
  src.clear()
  print("You said : " +  user_audio_text)
  src.send_keys(user_audio_text[12:]) 
  src.send_keys(Keys.ENTER)

def NikkiWeather():                                       # this function tell weather  
  mn = user_audio_text.find('in')
  cloud = user_audio_text[mn+3:].lower()
  url = f'https://www.google.com/search?q=weather+{cloud}'
  page = requests.get(url).content
  soup = useMe(page,'lxml')
  r = open('x.html','w') 
  r.write(soup.prettify())
  data = soup.find('div',class_="kvKEAb")
  print(data.text)
  eng.say(data.text)
  eng.runAndWait()

print(''' 
    hello this is Nikki assistant 
    i will answer your questions ?
''')

eng.say('hello this is Nikki assistant. i am ready to help you')
eng.runAndWait()
error = 1
while True:
  try:  
    user_audio_text = NikkiVoiceSource()
    print("You said :" + user_audio_text)

    if 'Nikki' in user_audio_text:
        
        if 'back' in user_audio_text or 'exit' in user_audio_text:
            print('<<<<<<<<< Bye boss >>>>>>>>>>')
            eng.say(' Bye boss ')
            eng.runAndWait()
            break
        elif 'hi' in user_audio_text or 'hello' in user_audio_text:
            timeFun()
            NikkiWork()

        elif 'what about you' in user_audio_text or 'what about you' in user_audio_text:
            eng.say("i'm Nikki i born in june 13 2022 developed by Prem kumar he is very creative person because he created me i respect him ")
            eng.runAndWait()

        elif 'p***' in user_audio_text or 'sex videos' in user_audio_text :
            eng.say('what the hell you want man fuck your self >>>>>>>>')
            pass

        elif 'weather in' in user_audio_text:
            NikkiWeather() 

        elif 'open insta' in user_audio_text or "open Instagram" in user_audio_text:
            eng.say('ok boss ! wait i am opening Instagram ')
            eng.runAndWait()
            res = user_audio_text.find('Prem')
            if user_audio_text[res:res+4] == 'Prem':
                print('running')
                user_name = 'click_theworld1'
                password = 'prem@123'
                NikkiInsta(user_name,password)
            user_name = input('enter your userName :')
            password = input('enter the password :')
            NikkiInsta(user_name,password)

        elif 'what are you doing' in user_audio_text :
            print("i'm still learning new things !")
            eng.say("i'm still learning new things ")
            NikkiBoring() 

        elif 'feeling boring' in user_audio_text:
            NikkiBoring()

        elif 'how are you' in user_audio_text or 'how Nikki' in user_audio_text:
            print("i'm doing great what about you : ")
            eng.say("i'm doing great what about you")
            eng.runAndWait()

        elif 'play song' in user_audio_text or 'song in spotify'  in user_audio_text:
            eng.say('ok boss ! wait i am opening spotify ')
            eng.runAndWait()
            NikkiPlaySong()

        elif 'open YouTube' in user_audio_text or 'YouTube' in  user_audio_text and 'play' in user_audio_text and 'Nikki' in user_audio_text:
            eng.say('ok boss ! wait i am opening browser')
            eng.runAndWait()
            value_ = user_audio_text.find('YouTube')
            song = user_audio_text[value_+8:]
            eng.say(f'ok boss finding{song}')
            eng.runAndWait()
            NikkiYoutube(song)

        elif 'time in' in user_audio_text  :
            mn = user_audio_text.find('in')
            timeL = user_audio_text[mn+3:].lower()
            NikkiTime(timeL)

        elif 'search' in user_audio_text or 'find' in user_audio_text or 'research' in user_audio_text:
            eng.say(' Bye boss ')
            eng.runAndWait()
            eng.say('ok boss')
            eng.runAndWait()
            NikkiSearch()

        elif 'who is' in user_audio_text:
            eng.say('ok boss')
            eng.runAndWait()
            NikkiWhoIs(user_audio_text[6:])
        
        elif 'any joke' in user_audio_text or 'tell' in user_audio_text and 'joke' in user_audio_text:
            r = random.randrange(0,len(joke_nik)-1)
            eng.say('ok boss')
            eng.runAndWait()
            eng.say(joke_nik[r])
            eng.runAndWait()

        elif "news today" in user_audio_text or 'today news' in user_audio_text:
            NikkiNewstoday()

        elif 'I love you' in user_audio_text or 'I love you' in user_audio_text :
            eng.say('hoo thank you i love you too')
            eng.runAndWait()

        elif 'wh' in user_audio_text:
            print('i am still learning--')
            eng.say('i am still learning --')
            eng.runAndWait()
        else:pass

    elif user_audio_text == 'what is your name' or user_audio_text in 'your name':
        print('\n >> hello my name is NIKKI/prem')
        eng.say('\t hello my name is NIKKI by prem')
        eng.runAndWait()

    elif 'how to use' in  user_audio_text or 'help' in user_audio_text:
        print("you can ask first you need to say 'NIKKI' After :play song, news today, any joke, who is, time in ,open YouTube,open insta,weather, ")
        eng.say("you can ask first you need to say 'NIKKI' After 'Nikki play song' , news today, any joke, who is, time in ,open YouTube,open insta,weather ")
        eng.runAndWait()
        
    else:
        print('tell Nikki name and ask anything')
        eng.say('tell Nikki name and ask anything')
        eng.runAndWait()

  except sr.UnknownValueError:
    print('Could not understand audio')
    eng.say('Could not understand audio')
    eng.runAndWait()
    if error > 2:
      s = 0
      while True:
        try:
            r = sr.Recognizer()                                                                               
            with sr.Microphone() as source:                                                                       
              print("--- >>")                                                                               
              audio = r.listen(source)   
            user_audio_text = r.recognize_google(audio)
            print("You said :" + user_audio_text)
            if 'hello Nikki' in user_audio_text or 'are you there' in user_audio_text or 'hi Nikki ' in user_audio_text:
              eng.say('Hello boss i here to help you ____')
              eng.runAndWait()
              error =1
              break
            else:
              print('\n tell Nikki')
              eng.say('ho hooo hoo')
              eng.runAndWait()
              s+=1
        except sr.UnknownValueError:
          s+=1 
          if s == 25:
            eng.say('Hello boss i here to help you')
            eng.runAndWait()
            r = random.randrange(0,len(joke_nik)-1)
            if r %2==0:
              eng.say(joke_nik[r])
              eng.runAndWait()
            s=0
    else:
      error+=1

  except sr.RequestError:
      print("Could not request results")
      pass

  except :
    print('hoho ')
    eng.say('hoohohoo')
    eng.runAndWait()
    pass
