from lib2to3.pgen2 import driver
import time
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
driver = webdriver.Chrome(executable_path="/home/navgurukul/Downloads/chromedriver-sel/chromedriver") 

class nikki():
  def __init__(self):
     pass
  def NikkiVoiceSource(sr,eng):
      r = sr.Recognizer()                                                       
      with sr.Microphone() as source:                                                  
          print("Listening… :")  
          eng.say('Listening…')
          eng.runAndWait()                         
          audio = r.listen(source)  
      return r.recognize_google(audio)

  def NikkiPlaySong(song):
    # song1 = ' '.join(song)
    song1 = song.replace(' ','+')
    driver.switch_to.new_window()
    driver.get(f'https://music.youtube.com/search?q={song1}')
    # driver.find_element_by_link_text()
    
  def NikkiYoutube(src_youtube):
    driver.switch_to.new_window()
    driver.get(f'https://www.youtube.com/')
    src2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))
    src2.send_keys(src_youtube) 
    time.sleep(2)
    src2.send_keys(Keys.ENTER)

  # def NikkiBoring():
  #     while True:
  #       try:
  #           eng.say("what about you Boss :")
  #           eng.runAndWait()
  #           myans = nik.NikkiVoiceSource(sr,eng)
  #           if 'boring' in myans:
  #             eng.say('if you want i will play something on youtube and jokes for you ')
  #             eng.runAndWait()
  #             ply = nik.NikkiVoiceSource(sr,eng)
  #             print('you say :',ply)
  #             list_play = ['telugu songs','ellie goulding','chaganti koteswara rao speeches mahabharatham etv','SriGarikipatiNarasimhaRaoOfficial','summer ball 2022']
  #             cho = random.choice(list_play)
  #             if 'YouTube' in ply:
  #                 nik.NikkiYoutube(cho)
  #                 break
  #             elif 'joke' in ply :
  #                 nik.NikkiNewstoday()
  #                 break
  #             elif 'you play' in ply:
  #                 res = ply.find('you play')+8
  #                 nik.NikkiYoutube(ply[res:])

  #           elif 'fine' in myans:
  #               eng.say('great to hear from you')
  #               eng.runAndWait()
  #               break
  #           else:
  #               eng.say('hohoho i dont what you mean !!')
  #               eng.runAndWait()
  #       except sr.UnknownValueError:
  #           print('Could not understand audio')
  #           eng.say('Could not understand audio')
  #           eng.runAndWait()
  #           pass

  def timeFun():
    t = nik.NikkiTime('india')
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

  def NIkkiblog():
    print('Blog time')
    driver.get('https://exploring-blog-app.herokuapp.com')
    not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='forEmail']")))
    not_now3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='forPassword']")))
    not_now2.send_keys('mynikki007@gmail.com')
    not_now3.send_keys('nikki@123')
    log_in = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type = 'submit']"))).click()  
    time.sleep(2)
    post = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type = 'button']"))).click()  
    tit =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='forText']"))).send_keys("Hello i'm NIkki by prem")
    tit2 =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='forTextarea']"))).send_keys("this is my first meet with the dlog bro nice to meet you bro")

  def NikkiInsta(username,password):                                     # this function do , auto login instagram     Post Blog
    driver.switch_to.new_window()          
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

  def NikkiSearch(user_audio_text):
    driver.switch_to.new_window()                                         # this function search anything in the browser
    driver.get('https://www.google.com/')
    src = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='q']")))
    src.clear()
    print("You said : " +  user_audio_text)
    src.send_keys(user_audio_text[12:]) 
    src.send_keys(Keys.ENTER)

  def NikkiWeather(user_audio_text):                                       # this function tell weather  
    mn = user_audio_text.find('in')
    cloud = user_audio_text[mn+3:].lower()
    url = f'https://www.google.com/search?q=weather+{cloud}'
    page = requests.get(url).content
    soup = useMe(page,'lxml')
    r = open('x.html','w') 
    r.write(soup.prettify())
    data = soup.find('div',class_="kvKEAb")

    eng.say(data.text)
    eng.runAndWait()
    mn = user_audio_text.find('in')

nik = nikki()
if '__main__' == __name__:
  print('this is my lis')
  eng.say('ok Boss')
  eng.runAndWait()
  # nik.NikkiNewstoday()
  # nik.NikkiPlaySong('burn')
  # nik.NikkiSearch('what is pyhton')
  # nik.NikkiWhoIs('pm')
  # nik.NikkiTime('usa')
  # nik.NikkiWeather('odisha')
  # nik.NikkiYoutube('telugu songs')
  # call.nikki.NikkiClass('with')
  # nik.NikkiInsta('click_theworld1','prem@63')
  # nik.NikkiWork()
  nik.NikkiBoring()
  print('tell Nikki name and ask anything')