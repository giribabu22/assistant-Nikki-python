import os
from sub_task.NikkiSay import NikkiSay

try:
    from dotenv import load_dotenv
    import speech_recognition as sr
    import time,random,json,requests
    from bs4 import BeautifulSoup as useMe
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    from playsound import playsound
    from pyautogui import press, hotkey
    import psutil
    from datetime import datetime
    import re
except ImportError:
    os.system('sudo apt-get install python3-tk python3-dev')
    os.system('pip install bs4')
    os.system('pip install selenium')
    os.system('pip install ib2to3')
    os.system('pip install speechRecognition')
    os.system('pip install playsound')
    os.system('pip install psutil')
    os.system('pip install pyautogui')
    os.system('pip install python-dotenv')
    os.system('sudo apt-get install jackd')
    os.system('jackd -d alsa')

error = 1
load_dotenv()

joke_nik = [['I invented a new word!Plagiarism!],[Did you hear about the mathematician who’s afraid of negative numbers?He’ll stop at nothing to avoid them.'], ['Why do we tell actors to “break a leg?”Because every play has a cast. Here are some dark jokes to check out if you have a morbid sense of humor.'], ['Helvetica and Times New Roman walk into a bar.“Get out of here!” shouts the bartender. “We don’t serve your type.”],[Yesterday I saw a guy spill all his Scrabble letters on the road. I asked him, “What’s the word on the street?”Once my dog ate all the Scrabble tiles. For days he kept leaving little messages around the house. Don’t miss these hilarious egg puns that will absolutely crack you up.'], ['Knock! Knock! Who’s there? Control Freak. Con… OK, now you say, “Control Freak who?”'], ['Hear about the new restaurant called Karma? There’s no menu: You get what you deserve.'], ['A woman in labor suddenly shouted, “Shouldn’t! Wouldn’t! Couldn’t! Didn’t! Can’t!”“Don’t worry,” said the doc. “Those are just contractions.”'], [
    'A bear walks into a bar and says, “Give me a whiskey and … cola.” “Why the big pause?” asks the bartender. The bear shrugged. “I’m not sure; I was born with them.”'], ['Did you hear about the actor who fell through the floorboards?He was just going through a stage.'], ['Did you hear about the claustrophobic astronaut? He just needed a little space.'], ['Why don’t scientists trust atoms? Because they make up everything.'], ['Why did the chicken go to the séance?To get to the other side. Check out these other “why did the chicken cross the road?” jokes for more laughs.'], ['Where are average things manufactured?The satisfactory.'], ['How do you drown a hipster? Throw him in the mainstream.'], ['What sits at the bottom of the sea and twitches?A nervous wreck.'], ['What does a nosy pepper do? Gets jalapeño business!'], ['How does Moses make tea? He brews.'], ['Why can’t you explain puns to kleptomaniacs?They always take things literally.'], ['How do you keep a bagel from getting away?Put lox on it.'], ['A man tells his doctor, “Doc, help me. I’m addicted to Twitter!”The doctor replies, “Sorry, I don’t follow you …”']]


class Nikki_functions_class():
    def __init__(self, driver, main_path):
        self.main_path = main_path
        self.f = open(f'{self.main_path}Manage_file/time_for_meeting.json')
        self.f2 = open(f'{self.main_path}Manage_file/main_save.json')
        self.time_table_data = json.load(self.f)
        self.main_file = json.load(self.f2)
        self.flag = 'unmute'
        self.NikkiSay = NikkiSay
        self.driver = driver
        self.last_time = datetime.now()
        self.last_hour = self.main_file[1]
        self.new_day = 0
        self.netError = 0
        self.out_put = 0
        self.sensorsBatery = 0
        self.r = sr.Recognizer()
        self.great_mes = ['Wow i have you', "Keep smiling, because life is a beautiful thing and there's so much to smile about.",
                          "Life is a long lesson in humility.", "In three words I can sum up everything I've learned about life. I love myself.",
                          "Love the life you live.", "Life is either a daring adventure or nothing at all"]
        # return 'uttran_'

    def display_frontend(self):
        self.driver.get(f'file://{self.main_path}views/front_nikki.html')

    def NikkiVoiceSource(self):
        try:
            with sr.Microphone() as source:
                audio = self.r.listen(source,phrase_time_limit=3)
            words = self.r.recognize_google(audio)
            return words

        except sr.RequestError as e:
            if self.netError < 3:
                self.NikkiSay('Boss, Network error check you wifi ')
                self.netError += 1

    def NikkiQuickVoice(self):
        if self.out_put < 4:
            playsound(f'{self.main_path}Manage_file/nice notification.mp3')
            with sr.Microphone() as source:
                audio = self.r.listen(source,phrase_time_limit=6)
                self.out_put += 1
                return self.r.recognize_google(audio)

    def NIkkiblog(self):
        self.driver.switch_to.new_window()
        self.driver.get('https://exploring-blog-app.herokuapp.com')
        not_now2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='forEmail']")))
        not_now3 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='forPassword']")))
        not_now2.send_keys('mynikki007@gmail.com')
        not_now3.send_keys('nikki@123')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type = 'submit']"))).click()
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type = 'button']"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[id='forText']"))).send_keys("Hello i'm NIkki by prem")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='forTextarea']"))).send_keys(
            "this is my first meet with the dlog bro nice to meet you bro")
        
    def NikkiPlaySong(self,user_audio_text):
        driver = self.driver
        pattern = r'(play songs in YouTube music|needle|music|play)\s+(.*)'
        match = re.search(pattern, user_audio_text, re.IGNORECASE)
        if match:
            song = match.group(2)
        else:
            l = user_audio_text.split()
            song = ' '.join(l[3:])
        self.NikkiSay(f'ok Boss. wait i am opening youtube music and playing {song}')
        song = song.replace(' ', '+')
        l = driver.window_handles
        for handle in l:
            driver.switch_to.window(handle)
            self.NikkiSay('YouTube Music in driver.title: ','YouTube Music' in driver.title)
            if 'YouTube Music' in driver.title:
                try:
                    hotkey('ctrl', 'w')
                    time.sleep(1)
                    press('enter')
                except Exception as e:
                    print(e)
                    # self.NikkiSay(e)
                time.sleep(1)
                break

        driver.switch_to.window(driver.window_handles[0])
        driver.switch_to.new_window()
        driver.get(f"https://music.youtube.com/search?q={song}")
        # Play the song
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "yt-icon[class ='icon style-scope ytmusic-play-button-renderer']"))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "tp-yt-paper-icon-button[class='player-minimize-button style-scope ytmusic-player']"))).click()
            out_put = 6
        except Exception as e:
            self.NikkiSay('Boss, something wrong in play song function.')

    def NikkiYoutube(self, src_youtube):
        # try:
        self.NikkiSay('ok boss ! wait i am opening youtube')
        res = src_youtube.replace(' ', '+')
        self.driver.switch_to.new_window()
        if len(src_youtube) > 0:
            self.driver.get(
                f'https://www.youtube.com/results?search_query={res}')
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "yt-formatted-string[class ='style-scope ytd-video-renderer']"))).click()
        else:
            self.driver.get(f'https://www.youtube.com/')
        # except:
        #     self.NikkiSay('Boss, error in Nikki Youtube function.')

    def NikkiBoring(self, r=True):
        list_play = ['telugu songs', 'ellie goulding', 'chaganti koteswara rao speeches mahabharatham etv',
                     'SriGarikipatiNarasimhaRaoOfficial', 'summer ball 2022', '']
        c = 0

        while r:
            try:
                c += 1
                self.NikkiSay(
                    'if you want i will play something on youtube, News, book for read and movie for watch')
                ply = self.NikkiVoiceSource()
                if c > 3:
                    r = False
                if 'YouTube' in ply:
                    cho = random.choice(list_play)
                    self.NikkiYoutube(cho)
                    r = False
                elif 'News' in ply:
                    self.NikkiNewstoday()
                    r = False
                elif 'you play' in ply:
                    res = ply.find('you play')+8
                    self.NikkiYoutube(ply[res:])
                    r = False
                elif 'movie' in ply:
                    self.NikkiSay('Boss, i am playing movie for you.')
                    self.driver.get('https://ww16.ibomma.bar/telugu-movies')
                    r = False
                elif 'book' in ply:
                    res = ply.find('book') + 9
                    self.Nikkibook(ply[res:])
                    r = False
                else:
                    r = True
            except sr.UnknownValueError:
                self.NikkiSay('Could not understand audio')
                if c > 3:
                    r = False
                pass
            except:
                pass
        return r

    def NikkiFeelTalk(self):
        r = True
        c2 = 0
        while r:
            try:
                c2 += 1
                self.NikkiSay("what about you Boss ")
                myans = self.NikkiVoiceSource()
                if c2 > 3:
                    r = False
                if 'boring' in myans:
                    r = self.NikkiBoring(r)
                elif 'fine' in myans or 'great' in myans:
                    self.NikkiSay('great to hear from you')
                    r = False
                else:
                    self.NikkiSay('what you mean Boss!!')
            except sr.UnknownValueError:
                self.NikkiSay('Could not understand audio')
                if c2 > 3:
                    r = False
                pass
            except:
                pass

    def NikkiGreatings(self):
        # try:
        t = datetime.now().hour
        res = 'good '

        if t >= 1 and t <= 11:
            res = 'good morning'
        elif t >= 12 and t <= 15:
            res = 'good afternoon'
        elif t >= 16 and t <= 22:
            res = 'good evening'

        self.NikkiSay(f'{res}')
        # except:
        #     self.NikkiSay('Boss, error in Greatings')

    # this function help, to find the who is questions

    def NikkiWhoIs(self, user_audio_text):
        last_url = str(user_audio_text).replace(' ', '+')
        url = 'https://www.google.com/search?q='+last_url
        page = requests.get(url).text
        soup = useMe(page, 'lxml')
        data = soup.prettify()
        r = soup.find('div', class_="kCrYT").getText()
        self.NikkiSay(r)

    def NikkiMute(self, user_audio_text):
        if 'mute' in user_audio_text and len(user_audio_text) == 4 or user_audio_text[:5] == 'sleep':
            self.flag = 'mute'
            self.NikkiSay("i am mute But i am waiting for you boss")
            self.out_put = 5

        elif 'Unmute' in user_audio_text:
            self.flag = 'Unmute'
            self.NikkiSay("i am unmute know")
            self.out_put = 0
        return self.flag

    def NikkiReminder(self, do='w', data=None):
        if do == 'r':
            with open(f'{self.main_path}Manage_file/time_for_meeting.json', 'r') as f5:
                res = json.dumps(f5)
            for i in res:
                self.NikkiSay(
                    f"{i} meeting you have at {res[i]['starting_time']}")
        # if do == 'w':
        #     self.NikkiSay(data)
        #     f = open('/home/navgurukul/Desktop/workOftheday.txt','a')
        #     f.write(data)

    def NikkiTranslation(self, word):
        self.NikkiSay('ok boss opening  translate')
        self.driver.switch_to.new_window()
        self.driver.get(
            'https://translate.google.co.in/?sl=en&tl=te&op=translate')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "textarea[class ='er8xn']"))).send_keys(word)

    # this function tell time

    def NikkiTime(self, timeL):
        url = f'https://www.google.com/search?q=time+{timeL}'
        page = requests.get(url).content
        soup = useMe(page, 'lxml')
        data = soup.find('div', class_="BNeawe iBp4i AP7Wnd")
        self.NikkiSay(f'time in {timeL,data.text}')
        return data.text, int(data.text[:-6])

    def NikkiNewstoday(self):
        latestNews = []
        url = 'https://www.ndtv.com/latest'
        page = requests.get(url).text
        soup = useMe(page, 'lxml')
        d = soup.findAll('div', class_="news_Itm")
        r = random.randrange(0, len(d)-1)
        for i in d:
            latestNews.append(i.text)
        if latestNews[r] in 'window._taboola ':
            del latestNews[r]
        self.NikkiSay(f'this is today news-paper {latestNews[r]}')

    def NikkiQuickQuestion(self, word='keyword'):
        while True:
            self.out_put = 0
            self.NikkiSay(f'What is the {word}. Boss')
            try:
                words = self.NikkiQuickVoice()
                if 'stop it' not in words:
                    return words
            except:
                pass

    def NikkiSearch(self, search_in):
        if 'keyword' in search_in:
            keywords = search_in[search_in.find('word')+5::]
        elif 'search' in search_in:
            keywords = search_in[search_in.find('search')+7::]
        else:
            keywords = self.NikkiQuickQuestion()
        keywords = keywords.replace(' ', '+')

        self.NikkiSay(
            f'ok boss i am opening google for you, finding {keywords}')
        self.driver.switch_to.new_window()
        try:                                   # this function search anything in the browser  LGOjhe
            url = f'https://www.google.com/search?q={keywords}'

            self.driver.get(url)
            # page = requests.get(url).content
            # soup = useMe(page,'lxml')
            # r    = open('x.html','w')
            # r.write(soup.prettify())
            # data = soup.find('div',class_="LGOjhe")
            # self.NikkiSay(data)
        except:
            self.NikkiSay('error in Nikki google search')

    # this function tell weather
    def NikkiWeather(self, cloud):
        url = f'https://www.google.com/search?q=weather+{cloud}'
        page = requests.get(url).content
        soup = useMe(page, 'lxml')
        data = soup.find('div', class_="kvKEAb")
        self.NikkiSay(f'weather in {cloud,data.text}')

    def NikkiCallBack(self, error, TrueFalse=True):

        self.NikkiAutoJoinMeeting()
        user_audio_text = self.NikkiVoiceSource()
        if 'hello Nikki' in user_audio_text or 'are you there' in user_audio_text or 'hai Nikki' in user_audio_text or 'are there' in user_audio_text:
            # self.eng.setProperty('volume', self.voice_save_file[0]['volume'])
            self.NikkiSay('Hello boss i here for you.')
            self.out_put = 0
            error = 1
            TrueFalse = False
        if 'Nikki' in user_audio_text:
            self.NikkiWritingHistory(user_audio_text)
            if 'stop music' in user_audio_text or 'playback' in user_audio_text or 'drop my needle' in user_audio_text or 'put the needle' in user_audio_text:
                # self.eng.setProperty(
                # 'volume', self.voice_save_file[0]['volume'])
                self.NikkiPlayback()
                # self.eng.setProperty('volume', 0)
            elif 'search' in user_audio_text or 'Google' in user_audio_text or 'keyword' in user_audio_text:
                self.NikkiSearch(user_audio_text)
            elif ('play' in user_audio_text and 'YouTube music' in user_audio_text) or ('play ' in user_audio_text and ('music' in user_audio_text) or 'song' in user_audio_text):
                self.NikkiPlaySong(user_audio_text)

        elif 'mute' in user_audio_text or 'Unmute' in user_audio_text:
            self.NikkiMute(user_audio_text)
            if 'Unmute' in user_audio_text:
                # self.eng.setProperty('volume', self.voice_save_file[0].volume)
                self.NikkiSay('i am in sleep mood')
                # self.NikkiMute
                # self.eng.setProperty('volume', 0)
                error = 0
                TrueFalse = True
        # else:
        #     error=0
        #     TrueFalse = True
        return error, TrueFalse

    def NikkiPlayback(self):
        self.NikkiSay('ok Boss ')
        li = self.driver.window_handles
        if len(li) > 1:
            for i in range(len(li)):
                c = self.driver.window_handles[i]
                self.driver.switch_to.window(c)
                if 'YouTube Music' in self.driver.title:
                    time.sleep(0.5)
                    press('SPACE')
                    break

    def NikkiCloseTab(self, tabName, user_audio_text):
        self.NikkiSay('ok Boss ')
        # c = self.driver.window_handles[0]
        li = self.driver.window_handles
        tabName = ''
        if 'stop music' in user_audio_text or 'back' in user_audio_text:
            tabName = 'YouTube music'
        if len(li) > 1:
            for i in range(len(li)):
                c = self.driver.window_handles[i]
                self.driver.switch_to.window(c)
                if 'YouTube Music' in self.driver.title:
                    time.sleep(0.5)
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, "yt-icon[class ='icon style-scope ytmusic-play-button-renderer']"))).click()
                    break
            else:
                try:
                    if user_audio_text[-1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                        c = self.driver.window_handles[int(
                            user_audio_text[-1])]
                        self.driver.switch_to.window(c)
                    time.sleep(1)
                    hotkey('ctrlleft', 'w')
                    press('enter')
                    # WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"yt-icon[class ='icon style-scope ytmusic-play-button-renderer']"))).click()
                except:
                    pass

        else:
            self.NikkiSay('all tabs are closed boss')

    def Nikkibook(self, book):
        self.NikkiSay('wait boss i am finding your asking book')
        self.driver.switch_to.new_window()
        self.driver.get(f'https://www.google.com/search?tbm=bks&q={book}')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div[class='VvrH3b']"))).click()

    def NikkiFrontEnd(self):
        # try:
        self.NikkiSay('wait boss setting the broser it will take few seconds')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = '/snap/bin/brave'
        chrome_options.add_argument('--remote-debugging-port=9000')
        self.driver = webdriver.Chrome(
            self.main_path+'chromedriver-sel/chromedriver', chrome_options=chrome_options)
        self.driver.get(f'file://{self.main_path}views/front_nikki.html')
        # except:
        #     self.NikkiSay('error in Nikki frontEnd')

    def NikkiWritingHistory(self, user_audio_text):
        # try:
        dic = {}
        with open(f'/{self.main_path}historyDataOfNikki/History_nikki.txt', 'r') as f:
            f2 = f.read()
        with open(f'/{self.main_path}historyDataOfNikki/History_nikki.txt', 'a') as f:
            f.write(' '+user_audio_text+' \n')
        with open(f'/{self.main_path}historyDataOfNikki/History_nikki.txt', 'r') as f:
            f2 = f.read()

        li = f2.split(' ')
        for word in li:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
        del dic['\n']

        li = list(dic.values())
        li.sort(reverse=True)
        newDict = {}

        for ele in li:
            for k, v in dic.items():
                if ele == v:
                    newDict[k] = v
        with open(f'/{self.main_path}historyDataOfNikki/mostlyUseWords.json', 'w') as f1:
            f1.write(json.dumps(newDict, indent=3))
        # except:
        #     self.NikkiSay('error in Nikki Writing History')

    def NikkiMeeting(self, link):
        self.NikkiSay("Boss. Now i am opening the google meet.")
        self.driver.get(link)
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='Dismiss']"))).click()
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='Join now']"))).click()
        except:
            try:
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Ask to join']"))).click()
            except:
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Ask to join']"))).click()

    def NikkiSetGoogle(self, word='Nikki'):
        if not (self.checking_google_login()):
            if ('Nikki' in word):
                user = os.getenv('NikkiGmail')
                pin = os.getenv('NikkiPassword')
                say = 'ok boss sighin my google account for you'
            else:
                user = os.getenv('gmail')
                pin = os.getenv('password')
                say = 'ok boss sighin your google account'

            self.driver.implicitly_wait(15)
            self.NikkiSay(say)
            try:
                self.driver.get('https://accounts.google.com/v3/signin/identifier?dsh=S1879550735%3A1670299099229216&authuser=0&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3DOGB%26tab%3Dkk%26utm_medium%3Dapp&ec=GAlAwAE&hl=en&service=accountsettings&flowName=GlifWebSignIn&flowEntry=AddSession')
                self.driver.find_element(
                    By.CSS_SELECTOR, "input#identifierId").send_keys(user)
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Next']"))).click()
                self.driver.find_element(By.NAME, 'Passwd').send_keys(pin)
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Next']"))).click()
                # if 'giri' in user :self.googleLog = 1
                time.sleep(1)
            except Exception as e:
                print(e, 'llllllllllllll')
                self.NikkiSay(
                    'Boss, something  wrong in login Google function.')
        else:
            self.NikkiSay('Boss, You already sign-in the google!')

    def NikkiAutoJoinMeeting(self):
        self.Nikkicharge()
        current_time = datetime.now()
        # print(current_time, self.last_hour, current_time.hour)
        if self.main_file[1] != current_time.hour and (current_time.hour in [12, 8, 14]):

            with open(f'{self.main_path}Manage_file/main_save.json', 'r') as f:
                self.main_file = json.load(f)

            self.main_file[1] = current_time.hour
            self.NikkiGoogleMeetDataCollect()

            with open(f'{self.main_path}Manage_file/main_save.json', 'w') as f:
                f.write(json.dumps(self.main_file, indent=3))

            # hotkey('ctrlleft', 'w')
            # time.sleep(0.4)
            # press('enter')
        if self.new_day != current_time.day:
            for d in self.time_table_data:
                with open(f'{self.main_path}Manage_file/time_for_meeting.json', 'a') as fil:
                    fil.write(json.dumps(d, indent=2))
            self.NikkiGreatings()
            g_mes = self.great_mes[random.randrange(0, len(self.great_mes)-1)]
            self.sensorsBatery = 0
            if current_time.strftime('%A') == 'Sunday':
                self.NikkiSay(
                    "Welcome Boss, Happy Sunday. Let this Sunday morning bring you lots of smiles, abd you’ll leave all of last week’s troubles behind you.")
            else:
                self.NikkiSay(g_mes)
            self.meetingEng = 0
            self.new_day = current_time.day

            for meet in self.time_table_data:
                self.time_table_data[meet]['status'] = False

            with open(f'{self.main_path}Manage_file/time_for_meeting.json', 'w') as f:
                f.write(json.dumps(self.time_table_data, indent=4))

        li12 = f'{current_time - self.last_time }'
        li12 = li12.split(':')
        if int(li12[0]) > 1 or int(li12[1]) > 5:
            # self.eng.setProperty('volume', self.voice_save_file[0]['volume'])
            self.NikkiSay(' I am activated. Boss ')
            # self.eng.setProperty('volume', 0)

        if self.last_time.minute != current_time.minute:
            with open(f'{self.main_path}Manage_file/time_for_meeting.json', "r") as file1:
                self.time_table_data = json.load(file1)
        if (current_time.strftime('%A') != 'Sunday'):
            for meet in self.time_table_data:
                starting_time = self.time_table_data[meet]['starting_time'].split(
                    ':')
                ending_time = self.time_table_data[meet]['ending_time'].split(
                    ':')

                if (current_time.hour >= int(starting_time[0]) and current_time.hour <= int(ending_time[0])) and not (self.time_table_data[meet]['status']):
                    if (current_time.hour == int(starting_time[0])) and current_time.minute <= int(starting_time[1]):
                        pass
                    elif (current_time.hour == int(ending_time[0]) and current_time.minute > int(ending_time[1])):
                        pass
                    elif (current_time.hour >= int(starting_time[0]) and current_time.hour <= int(ending_time[0])):

                        self.NikkiSay(
                            f'Boss, You have {meet} meeting you want to Join')
                        self.NikkiSetGoogle('Prem')
                        if 'meeting_link' in self.time_table_data[meet]:
                            self.NikkiMeeting(
                                f"https://meet.google.com/"+self.time_table_data[meet]['meeting_link'])
                            self.time_table_data[meet]['status'] = True
                        else:
                            self.time_table_data[meet]['status'] = True
                        with open(f'{self.main_path}Manage_file/time_for_meeting.json', 'w') as fil:
                            fil.write(json.dumps(
                                self.time_table_data, indent=2))
                        self.NikkiMute('sleep')
                        self.out_put = 6

        self.last_time = current_time

    def NikkiCreatingMeetingLink(self):
        self.NikkiSetGoogle()
        self.NikkiSay('Boss, created the google meeting link')
        self.NikkiMeeting('https://meet.google.com/maa-xbxm-gmi')
        self.NikkiMute('sleep')
        self.out_put = 6

    def Nikkicharge(self):
        s = int(psutil.sensors_battery()[0])
        if s <= 20 and self.sensorsBatery <= 2 or s <= 5 and self.sensorsBatery < 6:
            # self.eng.setProperty('volume', self.voice_save_file[0]['volume'])
            self.sensorsBatery += 1
            self.NikkiSay(f'{s}% Boss, My battery is low, Can charger me ')
            # self.eng.setProperty('volume', 0)
        elif s >= 22 and s <= 97 and self.sensorsBatery != 0:
            self.sensorsBatery = 0
        elif s >= 100 and self.sensorsBatery < 4:
            # self.eng.setProperty('volume', self.voice_save_file[0]['volume'])
            self.sensorsBatery += 1
            self.NikkiSay(
                f'{s}%.Boss, My battery is full. Can you remove my charging')
            # self.eng.setProperty('volume', 0)

    def NikkiCreatingNewProject(self):
        file_name = self.NikkiQuickQuestion('project name')
        self.NikkiSay('Boss. I am creating Folder ')
        file_name = file_name[file_name.find('name')+5:].replace(' ', '_')
        os.system(f'mkdir  /home/prem/Desktop/prjects/{file_name}')
        self.NikkiSay(
            'just a second Boss. I am opening the Visual Studio Code editer ')
        os.system(f'code  /home/prem/Desktop/prjects/{file_name}')

    def NikkiFolderExistOpen(self, names, word, path):
        dir_list = os.listdir(path)
        # print(dir_list)
        if "names" in word:
            self.NikkiSay('In this folder files names are')
            for name in names:
                self.NikkiSay(name)
        return dir_list

    def NikkiOpenVscode(self):
        word = self.NikkiQuickQuestion('exist file name')
        path = '/home/prem/Desktop/prjects/'
        dir_list = self.NikkiFolderExistOpen(dir_list, word, path)
        for project in dir_list:
            if word in project:
                self.NikkiSay(
                    f'just a second Boss. I am opening the Visual Studio Code editer file name {word}')
                word = self.NikkiQuickQuestion(
                    'yes or no, Do you want to open Visual studio')
                os.system(f'code  /home/prem/Desktop/prjects/{file_name}') if 'yes' in word or 's' in word else self.NikkiSay(
                    f'Thank you, i am not doing anything.')
                return None
        path = '/home/prem/Desktop/office_file'
        dir_list = self.NikkiFolderExistOpen(dir_list, word, path)
        # print(dir_list)
        for project in dir_list:
            if word in project:
                self.NikkiSay(
                    f'just a second Boss. I am opening the Visual Studio Code editer file name {word}')
                word = self.NikkiQuickQuestion(
                    'yes or no, Do you want to open Visual studio')
                os.system(f'code  /home/prem/Desktop/prjects/{file_name}') if 'yes' in word or 's' in word else self.NikkiSay(
                    f'Thank you, i am not doing anything.')
                return None
        # for project_name in dir_list:
        #     if word in project_name:
        if 'Sans' in word:
            os.system(f'code Desktop/office_file/sansaar/')  # TeleBot-Python

        elif 'bot' in word:
            self.NikkiSay(
                'just a second Boss. I am opening the Visual Studio Code editer ')
            os.system(f'code Desktop/office_file/TeleBot-Python')

        elif 'name' in 'word':
            file_name = word[word.find('name')+5:].replace(' ', '_')
            self.NikkiSay(f"I am making the file with the name {file_name}")
            os.system(f'mkdir  /home/prem/Desktop/prjects/{file_name}')
            self.NikkiSay(
                'just a second Boss. I am opening the Visual Studio Code editer ')
            os.system(f'code  /home/prem/Desktop/prjects/{file_name}')
        else:
            self.NikkiSay(
                'Boss, what you mean. Just tell the name of the file, tell names for all exist folders names')

    def NikkiGoogleMeetDataCollect(self):
        self.driver.switch_to.new_window()
        self.driver.get("https://meet.google.com/")
        self.driver.implicitly_wait(15)
        elements = self.driver.find_elements(
            By.CSS_SELECTOR, "[class='wKIIs']")
        d = {}
        with open(f'{self.main_path}Manage_file/time_for_meeting.json', 'w') as fil:
            fil.write(json.dumps(d, indent=2))
        for element in elements:
            arialabel = element.get_attribute(
                "aria-label").replace('This meeting has started. ', '')
            databegintime = element.get_attribute("data-begin-time")
            dataendtime = element.get_attribute("data-end-time")
            datacallid = element.get_attribute("data-call-id")
            # dataisnow = element.get_attribute("data-is-now")

            # divide by 1000 to convert to seconds
            timestamp = int(databegintime) / 1000
            dt_object = datetime.fromtimestamp(timestamp)

            # divide by 1000 to convert to seconds
            timestamp2 = int(dataendtime) / 1000
            dt_object2 = datetime.fromtimestamp(timestamp2)
            d.update({arialabel: {"starting_time": dt_object.strftime("%H:%M:%S"),
                                  "ending_time": dt_object2.strftime("%H:%M:%S"), "meeting_link": datacallid, "status": False}})
        try:
            with open(f'{self.main_path}Manage_file/time_for_meeting.json', 'w') as fil:
                fil.write(json.dumps(d, indent=2))
            # hotkey('ctrlleft', 'w')
            # press('enter')
            # time.sleep(1)
            # li = self.driver.window_handles
            # self.driver.window_handles[len(li)-1]
        except Exception as e:
            print(e)

    def checking_google_login(self):
        self.driver.switch_to.new_window()
        self.driver.get('https://myaccount.google.com/')
        try:
            h1 = self.driver.find_element(By.CLASS_NAME, 'XY0ASe').text
            if 'Welcome,' in h1:
                return True
        except Exception as e:
            return False

    # def NikkiDatafromApi(self):
    #     data = requests.get('https://doeslist.herokuapp.com/api/data').text
    #     page =  json.loads(data)
    #     # self.time_table_data = page['do_data']
    #     return page['do_data']

    # def NikkiAutoEnglishClassJoin(self):
    #     if not(self.googleLog):
    #         self.googleLog = 1
    #         self.NikkiSetGoogle()
    #     self.meetingEng = 1
    #     self.NikkiSay('Boss, You have english meeting you want to Join')
    #     self.NikkiMeeting('https://meet.google.com/kkj-djxf-usn')
    #     self.NikkiMute('sleep')
