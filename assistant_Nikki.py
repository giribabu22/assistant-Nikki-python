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

from distutils.log import error
from gettext import find
from subprocess import call
import speech_recognition as sr
import requests,time,random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup as useMe
import pyttsx3

joke_nik = [['I invented a new word!Plagiarism!],[Did you hear about the mathematician who’s afraid of negative numbers?He’ll stop at nothing to avoid them.'],['Why do we tell actors to “break a leg?”Because every play has a cast. Here are some dark jokes to check out if you have a morbid sense of humor.'],['Helvetica and Times New Roman walk into a bar.“Get out of here!” shouts the bartender. “We don’t serve your type.”],[Yesterday I saw a guy spill all his Scrabble letters on the road. I asked him, “What’s the word on the street?”Once my dog ate all the Scrabble tiles. For days he kept leaving little messages around the house. Don’t miss these hilarious egg puns that will absolutely crack you up.'],['Knock! Knock! Who’s there? Control Freak. Con… OK, now you say, “Control Freak who?”' ],['Hear about the new restaurant called Karma? There’s no menu: You get what you deserve.'],['A woman in labor suddenly shouted, “Shouldn’t! Wouldn’t! Couldn’t! Didn’t! Can’t!”“Don’t worry,” said the doc. “Those are just contractions.”'],['A bear walks into a bar and says, “Give me a whiskey and … cola.” “Why the big pause?” asks the bartender. The bear shrugged. “I’m not sure; I was born with them.”'],['Did you hear about the actor who fell through the floorboards?He was just going through a stage.'],['Did you hear about the claustrophobic astronaut? He just needed a little space.'],['Why don’t scientists trust atoms? Because they make up everything.'],['Why did the chicken go to the séance?To get to the other side. Check out these other “why did the chicken cross the road?” jokes for more laughs.'],['Where are average things manufactured?The satisfactory.'],['How do you drown a hipster? Throw him in the mainstream.'],['What sits at the bottom of the sea and twitches?A nervous wreck.'],['What does a nosy pepper do? Gets jalapeño business!'],['How does Moses make tea? He brews.'],['Why can’t you explain puns to kleptomaniacs?They always take things literally.'],['How do you keep a bagel from getting away?Put lox on it.'],['A man tells his doctor, “Doc, help me. I’m addicted to Twitter!”The doctor replies, “Sorry, I don’t follow you …”']]

# this is assistant voice creating 

eng = pyttsx3.init()
voices = eng.getProperty('voices')
eng.setProperty('voice', 'english_rp+f2') #my preference
eng.runAndWait()
eng.setProperty('volume', 4.0)


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


def NikkiInsta(username,password):                                     # this function do , auto login instagram            
  driver = webdriver.Firefox(executable_path="/home/navgurukul/Downloads/geckodriver-v0.31.0-linux64/geckodriver")
  driver.get('https://www.instagram.com/accounts/login/')
  user_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
  pas = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name = 'password']")))
  user_name.clear()
  pas.clear()
  print('loading....')
  user_name.send_keys(username)
  pas.send_keys(password)
  log_in = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type = 'submit']"))).click()  
  time.sleep(2)
  not_now2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()
  searchbox = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))

  searchbox.clear()

def NikkiTime(mn,timeL):                                    # this function tell time 
  url = f'https://www.google.com/search?q=time+{timeL}'
  page = requests.get(url).content
  soup = useMe(page,'lxml')
  data = soup.find('div',class_="BNeawe iBp4i AP7Wnd")
  print(data.text)
  eng.say(data.text)
  eng.runAndWait()

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
  time.sleep(10)
  driver.quit()

def NikkiYoutube(song):
  song = song.replace(' ','+')
  driver = webdriver.Firefox(executable_path="/home/navgurukul/Downloads/geckodriver-v0.31.0-linux64/geckodriver")
  driver.get(f'https://www.youtube.com/results?search_query={song}')
  src2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))
  src2.send_keys(song) 
  time.sleep(1)
  src2.send_keys(Keys.ENTER)

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
error = 0
while True:
  try:
    r = sr.Recognizer()                                                       
    with sr.Microphone() as source:                                                  
        print("Listening… :")  
        eng.say('Listening…')
        eng.runAndWait()                         
        audio = r.listen(source)   
    user_audio_text = r.recognize_google(audio)
    print("You said :" + user_audio_text)
    call_Nikki = user_audio_text.split()
    if 'Nikki' in user_audio_text and 'back' in user_audio_text or 'Nikki' in user_audio_text and 'exit' in user_audio_text:
      print('<<<<<<<<< Bye boss >>>>>>>>>>')
      eng.say(' Bye boss ')
      eng.runAndWait()
      break

    elif user_audio_text == 'Nikki what about you' or user_audio_text == 'Nikki what about you':
      eng.say("i'm Nikki i born in june 13 2022 developed by Prem kumar he is very creative person because he created me i respect him ")
      eng.runAndWait()

    elif 'p***' in user_audio_text or 'sex videos' in user_audio_text :
      eng.say('what the hell you want man fuck your self >>>>>>>>')
      pass

    elif user_audio_text[:13] == 'Nikki weather' :
      NikkiWeather()

    elif user_audio_text == 'what is your name' or user_audio_text in 'your name':
      print('\n >> hello my name is NIKKI/prem')
      eng.say('\t hello my name is NIKKI by prem')
      eng.runAndWait() 

    elif user_audio_text[:24]=='Nikki open insta account' or user_audio_text[:19] == "Nikki open Instagram ac ":
      eng.say('ok boss')
      eng.runAndWait()
      print('running',user_audio_text[25:])
      if user_audio_text[25:] == 'Prem':
        print('running')
        user_name = 'click_theworld1'
        password = 'prem@123'
        NikkiInsta(user_name,password)
      user_name = input('enter your userName :')
      password = input('enter the password :')
      NikkiInsta(user_name,password)

    elif user_audio_text == 'Nikki what are you doing' or user_audio_text == 'what are you doing':
      print("i'm still learning new things !")
      eng.say("i'm still learning new things")
      eng.runAndWait()

    elif user_audio_text == 'Nikki how are you' or user_audio_text == 'how are you'or user_audio_text == 'how are you Nikki':
      print("i'm doing great what about you : ")
      eng.say("i'm doing great what about you")
      eng.runAndWait()
      time.sleep(2)
    elif user_audio_text[:21] == 'Nikki play on YouTube' or 'YouTube' in  call_Nikki and 'play' in call_Nikki:
      value_ = user_audio_text.find('YouTube')
      song = user_audio_text[value_+8:]
      eng.say(f'ok boss finding{song}')
      eng.runAndWait()
      NikkiYoutube(song)

    elif user_audio_text[:13] in 'Nikki time in':
      mn = user_audio_text.find('in')
      timeL = user_audio_text[mn+3:].lower()
      NikkiTime(mn,timeL)

    elif user_audio_text[0:12] in 'Nikki search' or user_audio_text[0:12] =='Nicky search' or user_audio_text[0:11] =='Niki search':
      eng.say('ok boss')
      eng.runAndWait()
      NikkiSearch()

    elif user_audio_text[0:12] == 'Nikki who is':
      eng.say('ok boss')
      eng.runAndWait()
      NikkiWhoIs(user_audio_text[6:])
      
    elif user_audio_text == 'any joke' or user_audio_text in 'Nikki' and user_audio_text in 'tell' and user_audio_text in 'joke':
      r = random.randrange(0,len(joke_nik)-1)
      eng.say('ok boss')
      eng.runAndWait()
      eng.say(joke_nik[r])
      eng.runAndWait()
    elif "Nikki news" == user_audio_text :
      NikkiNewstoday()
    elif user_audio_text == 'Nikki I love you' or user_audio_text == 'I love you Nikki' :
      eng.say('hoo thank you i love you too')
      eng.runAndWait()

    elif  user_audio_text[0:2] != 'wh':
      print('i am still learning--')
      eng.say('i am still learning --')
      eng.runAndWait()
    else:
      pass

  except sr.UnknownValueError:
    eng.say('Could not understand audio')
    eng.runAndWait()
    if error > 2:
      s = 0
      while True:
        try:
            r = sr.Recognizer()                                                                               
            with sr.Microphone() as source:                                                                       
              print("…...... :")                                                                               
              audio = r.listen(source)   
            user_audio_text = r.recognize_google(audio)
            call_Nikki = user_audio_text.split()
            print("You said :" + user_audio_text)
            if s == 10:
              print('i am sleeping')
              time.sleep(20) 
            if user_audio_text in 'Nikki' or 'Nikki' in call_Nikki or 'ok' in call_Nikki:
              eng.say('Hello boss i here to help you ____ prem')
              eng.runAndWait()
              error =0
              break
            else:
              print('tell Nikki')
        except sr.UnknownValueError:
          s+=1 
          if s == 10:
                print('i am sleeping')
                time.sleep(10) 
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

  except sr.RequestError as e:
      print("Could not request results; {0}".format(e))

  except (error):
    print('hoho ')
    eng.say('hoohohoo')
    eng.runAndWait()
    pass
