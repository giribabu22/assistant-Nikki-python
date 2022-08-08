from lib2to3.pgen2 import driver
import time
from distutils.log import error
import speech_recognition as sr
import requests,random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup as useMe
import pyttsx3

eng      = pyttsx3.init()
voices   = eng.getProperty('voices')
flag     = 'unmute'
joke_nik = [['I invented a new word!Plagiarism!],[Did you hear about the mathematician who’s afraid of negative numbers?He’ll stop at nothing to avoid them.'],['Why do we tell actors to “break a leg?”Because every play has a cast. Here are some dark jokes to check out if you have a morbid sense of humor.'],['Helvetica and Times New Roman walk into a bar.“Get out of here!” shouts the bartender. “We don’t serve your type.”],[Yesterday I saw a guy spill all his Scrabble letters on the road. I asked him, “What’s the word on the street?”Once my dog ate all the Scrabble tiles. For days he kept leaving little messages around the house. Don’t miss these hilarious egg puns that will absolutely crack you up.'],['Knock! Knock! Who’s there? Control Freak. Con… OK, now you say, “Control Freak who?”' ],['Hear about the new restaurant called Karma? There’s no menu: You get what you deserve.'],['A woman in labor suddenly shouted, “Shouldn’t! Wouldn’t! Couldn’t! Didn’t! Can’t!”“Don’t worry,” said the doc. “Those are just contractions.”'],['A bear walks into a bar and says, “Give me a whiskey and … cola.” “Why the big pause?” asks the bartender. The bear shrugged. “I’m not sure; I was born with them.”'],['Did you hear about the actor who fell through the floorboards?He was just going through a stage.'],['Did you hear about the claustrophobic astronaut? He just needed a little space.'],['Why don’t scientists trust atoms? Because they make up everything.'],['Why did the chicken go to the séance?To get to the other side. Check out these other “why did the chicken cross the road?” jokes for more laughs.'],['Where are average things manufactured?The satisfactory.'],['How do you drown a hipster? Throw him in the mainstream.'],['What sits at the bottom of the sea and twitches?A nervous wreck.'],['What does a nosy pepper do? Gets jalapeño business!'],['How does Moses make tea? He brews.'],['Why can’t you explain puns to kleptomaniacs?They always take things literally.'],['How do you keep a bagel from getting away?Put lox on it.'],['A man tells his doctor, “Doc, help me. I’m addicted to Twitter!”The doctor replies, “Sorry, I don’t follow you …”']]

eng.setProperty('voice', 'english_rp+f3')
eng.setProperty('rate',150)
eng.setProperty('volume', 5.0)

def NikkiSay(data):
    eng.say(data)
    eng.runAndWait()

def NIkkiblog(driver):
  driver.get('https://exploring-blog-app.herokuapp.com')
  not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='forEmail']")))
  not_now3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='forPassword']")))
  not_now2.send_keys('mynikki007@gmail.com')
  not_now3.send_keys('nikki@123')
  WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type = 'submit']"))).click()  
  time.sleep(2)
  WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type = 'button']"))).click()  
  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='forText']"))).send_keys("Hello i'm NIkki by prem")
  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='forTextarea']"))).send_keys("this is my first meet with the dlog bro nice to meet you bro")

def NikkiVoiceSource():
    r = sr.Recognizer()                                                       
    with sr.Microphone() as source: 
        NikkiSay('Listening…')
        audio = r.listen(source) 
    return r.recognize_google(audio)

def NikkiPlaySong(song,driver):
  NikkiSay('ok boss ! wait i am opening youtube music ')
  driver.switch_to.new_window()
  driver.get(f'https://music.youtube.com/search?q={song}')
  WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"yt-icon[class ='icon style-scope ytmusic-play-button-renderer']"))).click() 
  time.sleep(7)
  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='ytp-ad-skip-button ytp-button']"))).click()
  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "tp-yt-paper-icon-button[class='player-minimize-button style-scope ytmusic-player']"))).click()

def NikkiYoutube(driver,src_youtube=''):
  NikkiSay('ok boss ! wait i am opening youtube')
  res = src_youtube.replace(' ','+')     
  driver.switch_to.new_window()
  if len(src_youtube) >0:
    driver.get(f'https://www.youtube.com/results?search_query={res}')
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"yt-formatted-string[class ='style-scope ytd-video-renderer']"))).click()
  else:
   driver.get(f'https://www.youtube.com/')

def NikkiBoring(r):
    list_play = ['telugu songs','ellie goulding','chaganti koteswara rao speeches mahabharatham etv','SriGarikipatiNarasimhaRaoOfficial','summer ball 2022']
    cho = random.choice(list_play)
    while r :
        NikkiSay('if you want i will play something on youtube,News and book for read for you')
        ply = NikkiVoiceSource()
        if 'YouTube' in ply:
            NikkiYoutube(cho)
            r = False
        elif 'News' in ply :
            NikkiNewstoday()
            r = False
        elif 'you play' in ply:
            res = ply.find('you play')+8
            NikkiYoutube(ply[res:])      
            r = False  
        elif 'book' in ply:
            res = ply.find('book')+9
            Nikkibook(ply[res:])
            r = False 
    return r

def NikkiClass(withlogin_ac,driver):
  driver.switch_to.new_window()
  driver.get('file:///home/navgurukul/Documents/Data%20Structures%20and%20Algorithms%20-%20Narasimha%20Karumanchi.pdf')
  NikkiSay('wait Boss i am opening Devsnest')
  if withlogin_ac == 'with':
    NikkiSetGoogle(driver)
    time.sleep(4)
    NikkiSay('sigh in your Devsnest account')
    driver.switch_to.new_window()
    driver.get(f'https://devsnest.in/login')
    time.sleep(3)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"span[class ='ml-3']"))).click()
  driver.switch_to.new_window()
  driver.get(f'https://www.youtube.com/c/Devsnest/videos')

def NikkiEng(driver): 
    NikkiSay('wait boss i am opening the google meeting')
    driver.get('https://meet.google.com/qrf-mkae-ayt')

def NikkiFeelTalk():
    r = True
    while r:
        try:
            NikkiSay("what about you Boss ")
            myans = NikkiVoiceSource()
            if 'boring' in myans:
                r = NikkiBoring(r)
            elif 'fine' in myans:
                NikkiSay('great to hear from you')
                r = False
            else:
                NikkiSay('what you mean Boss!!')
        except sr.UnknownValueError:
            NikkiSay('Could not understand audio')
            pass
        except:
            pass

def NikkiSetGoogle(driver,name):
    if 'prem' in name:
        user = 'giribabu22@navgurukul.org'
        pin = 'prem@630'
    else:
        user = 'mynikki007@gmail.com'
        pin = 'Nikki@630'
    NikkiSay('ok boss sighin your google account')
    driver.switch_to.new_window()
    driver.get('https://accounts.google.com/signin')
    driver.find_element(By.CSS_SELECTOR, "input#identifierId").send_keys(user)
    driver.find_element_by_xpath("//span[text()='Next']").click()
    time.sleep(3)
    driver.find_element(By.NAME, "password").send_keys(pin)
    driver.find_element_by_xpath("//span[text()='Next']").click()

def timeFun():
    res,t = NikkiTime('india')
    if t >= 1 and t <= 11 and 'am' in res:
        res = 'good morning'
    elif t == 12:
        if 'pm' in res:
            res = 'good afternoon'
        else:
            res = 'good night'
    elif t >= 1 and t <= 3 and 'pm' in res:
        res = 'good afternoon'
    elif t >= 4 and t <= 11 and 'pm' in res:
        res = 'good evening'
    else :
        res = 'good night'
    NikkiSay(f'Hello Boss {res}')

def NikkiWhoIs(user_audio_text):                                         # this function help, to find the who is questions
  last_url = str(user_audio_text).replace(' ','+')
  url = 'https://www.google.com/search?q='+last_url
  page = requests.get(url).text
  soup = useMe(page,'lxml')
  data =soup.prettify()
  r = soup.find('div' ,class_="kCrYT").getText()
  NikkiSay(r)

def NikkiMute(user_audio_text):
    if 'mute' in user_audio_text and len(user_audio_text) == 4 or user_audio_text[:5] == 'sleep':
        flag = 'mute'
        NikkiSay("i am mute But i am waiting for you boss")
        print("i am mute know")
        eng.setProperty('volume', 0)
    elif 'Unmute' in user_audio_text:
        voices = eng.getProperty('voices')
        eng.setProperty('voice', 'english_rp+f3')
        eng.setProperty('volume', 5.0)
        flag = 'Unmute'
        NikkiSay("i am unmute know")
    return flag

def NikkiWork():
    f = open('/home/navgurukul/Desktop/workOftheday.txt')
    res = f.read()
    NikkiSay(res)

def NikkiTranslation(word,driver):
  NikkiSay('ok boss opening  translate')
  driver.switch_to.new_window()
  driver.get('https://translate.google.co.in/?sl=en&tl=te&op=translate')
  WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"textarea[class ='er8xn']"))).send_keys(word)
  

def NikkiInsta(username,password,driver):                                     # this function do , auto login instagram 
  NikkiSay('ok boss wait i am opening Instagram')
  driver.switch_to.new_window()           
  driver.get('https://www.instagram.com/accounts/login/')
  user_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))).clear()
  user_name.send_keys(username)
  pas = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name = 'password']"))).clear()
  pas.send_keys(password)
  WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type = 'submit']"))).click() 
  time.sleep(2)
  WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()
  WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()
  searchbox = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))
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
  NikkiSay(f'time in {timeL,data.text}')
  return data.text,int(data.text[:-6])

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
  NikkiSay(f'this is today news-paper {latestNews[r]}')

def NikkiSearch(search_in,driver):                                    # this function search anything in the browser
  NikkiSay('ok boss i am opening google for you Boss')                                      
  driver.switch_to.new_window()
  driver.get('https://www.google.com/')
  src = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='q']")))
  src.clear()
  src.send_keys(search_in) 
  src.send_keys(Keys.ENTER)

def NikkiWeather(cloud):                                       # this function tell weather  
  url = f'https://www.google.com/search?q=weather+{cloud}'
  page = requests.get(url).content
  soup = useMe(page,'lxml')
  r = open('x.html','w') 
  r.write(soup.prettify())
  data = soup.find('div',class_="kvKEAb")
  NikkiSay(f'weather in{cloud,data.text}')

def Nikkibook(book,driver):
    NikkiSay('wait boss i am finding your asking book')
    driver.switch_to.new_window()
    ret = False
    if 'data' in book:
        driver.get('file:///home/navgurukul/Documents/Data%20Structures%20and%20Algorithms%20-%20Narasimha%20Karumanchi.pdf')
    elif 'JavaScript' in book:
        driver.get('file:///home/navgurukul/Documents/vdoc.pub_speaking-javascript-an-in-depth-guide-for-programmers.pdf')
    else:
        driver.get(f'https://www.google.com/search?tbm=bks&q={book}')
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[class='VvrH3b']"))).click()
                    
def NikkiCallBack(error,TrueFalse=True):
    user_audio_text = NikkiVoiceSource()
    if 'hello Nikki' in user_audio_text or 'are you there' in user_audio_text or 'hai Nikki' in user_audio_text or 'are there' in user_audio_text:
        eng.setProperty('voice', 'english_rp+f3')
        eng.setProperty('volume', 5.0)
        NikkiSay('Hello boss i here for you ___')
        error = 1
        TrueFalse = False
    elif 'mute' in user_audio_text or 'Unmute' in user_audio_text:
        NikkiMute(user_audio_text)
        if 'Unmute' in user_audio_text:
            NikkiSay('your in sleep mood')
    else:
        NikkiSay('this is try block')
        error=0
        s+=1
    return error,TrueFalse

def NikkiCloseTab(tabName,user_audio_text,driver):
  NikkiSay('ok Boss closing the tab')
  c = driver.window_handles[0]
  li = driver.window_handles
  if 'stop music' in user_audio_text :
    tabName = 'YouTube music'
  if len(li) > 1:
    for i in range(len(li)):
        if tabName == driver.title:
            c = driver.window_handles[i+1]
            driver.switch_to.window(c)
            driver.close()
            break
    else:
        if user_audio_text[-1] in ['1','2','3','4','5','6','7','8','9','0']:
            num = int(user_audio_text[-1])
            c = driver.window_handles[num]
            driver.switch_to.window(c)
        c = driver.window_handles[len(li)-1]
        driver.close()
  else:
    NikkiSay('all tabs are closed boss')

def NikkiopenJavascript(driver):
        driver.switch_to.new_window()
        driver.get('file:///home/navgurukul/Documents/vdoc.pub_speaking-javascript-an-in-depth-guide-for-programmers.pdf')