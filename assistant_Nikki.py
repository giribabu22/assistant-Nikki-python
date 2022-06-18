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
import speech_recognition as sr
import requests,time,os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup as useMe
import pyttsx3


# this is assistant voice creating 

eng = pyttsx3.init()
voices = eng.getProperty('voices')
eng.setProperty('voice', 'english_rp+f2') #my preference
eng.runAndWait()
eng.setProperty('volume', 5.0)


def NikkiWhoIs(user_audio_text):                                    # this function help, to find the who is questions

  last_url = str(user_audio_text).replace(' ','+')
  url = 'https://www.google.com/search?q='+last_url
  page = requests.get(url).text
  soup = useMe(page,'lxml')
  data =soup.prettify()
  r = soup.find('div' ,class_="kCrYT").getText()
  print(r)
  eng.say(r)
  eng.runAndWait()


def NikkiInsta(user_name,password):                                                    # this function do , auto login instagram
                
  driver = webdriver.Firefox(executable_path="/home/navgurukul/Downloads/geckodriver-v0.31.0-linux64/geckodriver")
  driver.get('https://www.instagram.com/accounts/login/')
  user_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
  password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name = 'password']")))
  user_name.clear()
  password.clear()
  print('loading....')
  user_name.send_keys(user_name)
  password.send_keys(password)

  log_in = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type = 'submit']"))).click()  
  not_now2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()
  searchbox = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))

  searchbox.clear()
  searchbox.clear()

  keyword = 'click_theworld1'
  searchbox.send_keys(keyword)
  time.sleep(5)
  searchbox.send_keys(Keys.ENTER)
  time.sleep(5)
  searchbox.send_keys(Keys.ENTER)
  time.sleep(5)
  follow2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[class = '_5f5mN       jIbKX  _6VtSN     yZn4P   ']"))).click()  


def NikkiTime(mn,timeL):                                    # this function tell time 

  url = f'https://www.google.com/search?q=time+{timeL}'
  page = requests.get(url).content
  soup = useMe(page,'lxml')
  data = soup.find('div',class_="BNeawe iBp4i AP7Wnd")
  print(data.text)
  eng.say(data.text)
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
while True:
  try:
    r = sr.Recognizer()                                                                               
    with sr.Microphone() as source:                                                                       
        print("Listening… :")  
        eng.say('Listening…')
        eng.runAndWait()                                                                                 
        audio = r.listen(source)   
    user_audio_text = r.recognize_google(audio)
    print(user_audio_text)
    print("You said :" + user_audio_text)

    if 'Nikki' in user_audio_text and 'back' in user_audio_text or 'Nikki' in user_audio_text and 'exit' in user_audio_text:
      print('<<<<<<<<< Come Again >>>>>>>>>>')
      break

    elif user_audio_text == 'what about you' or user_audio_text == 'Nikki what about you':
      print("i'm Nikki i born in june 13 2022. \n developed by Prem kumar. he is very creative person because he created me i respect him")
      eng.say("i'm Nikki i born in june 13 2022 developed by Prem kumar he is very creative person because he created me i love him ")
      eng.runAndWait()

    elif 'p***' in user_audio_text or 'sex videos' in user_audio_text :
      print(eng.say('what the hell you want man fuck your self >>>>>>>>'))
      pass

    elif user_audio_text[:13] == 'Nikki weather' :
      NikkiWeather()

    elif user_audio_text == 'what is your name' or user_audio_text in 'your name':
      print('\n >> hello my name is NIKKI/prem')
      eng.say('\t hello my name is NIKKI by prem')
      eng.runAndWait() 

    elif user_audio_text == "Nikki open Insta" or user_audio_text == "Nikki open Instagram":
      user_name = input('enter your userName :')
      password = input('enter the password :')
      NikkiInsta(user_name,password)

    elif user_audio_text == 'Nikki what are you doing' or user_audio_text == 'what are you doing':
      print("i'm still learning new things !")
      eng.say("i'm still learning new things")
      eng.runAndWait()

    elif user_audio_text == 'Nikki how are you' or user_audio_text == 'how are you':
      print("i'm doing great what about you : ")
      eng.say("i'm doing great what about you")
      eng.runAndWait()
      time.sleep(2)

    elif user_audio_text[:13] in 'Nikki time in':
      mn = user_audio_text.find('in')
      timeL = user_audio_text[mn+3:].lower()
      NikkiTime(mn,timeL)

    elif user_audio_text[0:12] in 'Nikki search' or user_audio_text[0:12] =='Nicky search' or user_audio_text[0:11] =='Niki search':
      NikkiSearch()

    elif user_audio_text[0:6] == 'who is':
      NikkiWhoIs(user_audio_text)

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
      print("Could not understand audio")
      eng.say('Could not understand audio')
      eng.runAndWait()

  except sr.RequestError as e:
      print("Could not request results; {0}".format(e))

  except :
    print('hoho ')
    eng.say('hoohohoo')
    eng.runAndWait()
    pass
