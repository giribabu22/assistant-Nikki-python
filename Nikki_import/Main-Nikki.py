# i used some modules in this projects like selenium,pyttsx3,speech recognition, Beautifulsoup,and some others
from tracemalloc import stop
from selenium import webdriver
import speech_recognition as sr
import Methodes_for_Nikki as call
import random
'''
                    //////// NIKKI ASSISTANT \\\\\\\\\\
                    ----------------------------------
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
6 ) if you ask play songs it will play songs for you 
7) it will open javascript book for you if you say "Nikki open Javascript book"
8) sighin your google account
    '''


call.NikkiSay('hello Boss welcome back')

joke_nik = [['I invented a new word!Plagiarism!],[Did you hear about the mathematician who’s afraid of negative numbers?He’ll stop at nothing to avoid them.'],['Why do we tell actors to “break a leg?”Because every play has a cast. Here are some dark jokes to check out if you have a morbid sense of humor.'],['Helvetica and Times New Roman walk into a bar.“Get out of here!” shouts the bartender. “We don’t serve your type.”],[Yesterday I saw a guy spill all his Scrabble letters on the road. I asked him, “What’s the word on the street?”Once my dog ate all the Scrabble tiles. For days he kept leaving little messages around the house. Don’t miss these hilarious egg puns that will absolutely crack you up.'],['Knock! Knock! Who’s there? Control Freak. Con… OK, now you say, “Control Freak who?”' ],['Hear about the new restaurant called Karma? There’s no menu: You get what you deserve.'],['A woman in labor suddenly shouted, “Shouldn’t! Wouldn’t! Couldn’t! Didn’t! Can’t!”“Don’t worry,” said the doc. “Those are just contractions.”'],['A bear walks into a bar and says, “Give me a whiskey and … cola.” “Why the big pause?” asks the bartender. The bear shrugged. “I’m not sure; I was born with them.”'],['Did you hear about the actor who fell through the floorboards?He was just going through a stage.'],['Did you hear about the claustrophobic astronaut? He just needed a little space.'],['Why don’t scientists trust atoms? Because they make up everything.'],['Why did the chicken go to the séance?To get to the other side. Check out these other “why did the chicken cross the road?” jokes for more laughs.'],['Where are average things manufactured?The satisfactory.'],['How do you drown a hipster? Throw him in the mainstream.'],['What sits at the bottom of the sea and twitches?A nervous wreck.'],['What does a nosy pepper do? Gets jalapeño business!'],['How does Moses make tea? He brews.'],['Why can’t you explain puns to kleptomaniacs?They always take things literally.'],['How do you keep a bagel from getting away?Put lox on it.'],['A man tells his doctor, “Doc, help me. I’m addicted to Twitter!”The doctor replies, “Sorry, I don’t follow you …”']]
import pyttsx3

eng      = pyttsx3.init()
error    = 1
netError = 0
call.NikkiSay('wait boss setting the broser it will take few seconds')
driver   = webdriver.Chrome(executable_path="/home/navgurukul/Downloads/chromedriver-sel/chromedriver")
driver.get('file:///home/navgurukul/Desktop/premlearn/nikki/front_nikki.html')

while True:
    try:
        user_audio_text = call.NikkiVoiceSource()
        call.NikkiSay(f'you asking : {user_audio_text}')
        if 'Nikki' in user_audio_text or 'Nicki' in user_audio_text  or 'ok' in user_audio_text:
            if 'open class' in user_audio_text or 'dsc class' in user_audio_text:
                res = 'open'
                if 'with' in user_audio_text:
                    res = 'with'
                call.NikkiClass(res,driver)
            elif ('play' in user_audio_text and 'YouTube music' in user_audio_text ) or ('play 'in user_audio_text and ('music' in user_audio_text) or 'song' in user_audio_text) :
                if 'play songs in YouTube music' in user_audio_text:
                    f = user_audio_text.find('music')+5
                    song = user_audio_text[f:]
                else:
                    l = user_audio_text.split()
                    song = ' '.join(l[3:])
                call.NikkiPlaySong(song,driver)

            elif 'English' in user_audio_text and 'class' in user_audio_text or 'English' in 'class':
                if 'with' in user_audio_text:
                    call.NikkiSetGoogle(driver,'prem')
                call.NikkiEng(driver)

            elif 'blog' in user_audio_text or 'blog app' in user_audio_text:
                call.NIkkiblog(driver)

            elif 'open YouTube' in user_audio_text or 'YouTube' in  user_audio_text :
                value_ = user_audio_text.find('YouTube')
                search_ = user_audio_text[value_+8:]
                call.NikkiYoutube(driver,search_)
                
            elif 'translate' in user_audio_text or 'what is in Telugu' in user_audio_text:
                if 'Telugu' in user_audio_text:
                    call.NikkiTranslation(''.join(user_audio_text[23:]),driver)
                else:
                    call.NikkiTranslation(''.join(user_audio_text[16:]),driver)
            elif 'search' in user_audio_text or 'Google' in user_audio_text:
                if 'ok' in user_audio_text:res = user_audio_text[2:]
                else:res = user_audio_text[13:]
                call.NikkiSearch(res,driver)

            elif 'hi' in user_audio_text or 'hello' in user_audio_text:
                call.timeFun()
                call.NikkiWork()

            elif 'what about you' in user_audio_text or 'what about you' in user_audio_text:
                call.NikkiSay("i'm Nikki i born in june 13 2022 developed by Prem kumar he is very creative person because he created me i respect him ")

            elif 'p***' in user_audio_text or 'sex videos' in user_audio_text :
                call.NikkiSay('what the hell you want man fuck your self')

            elif 'translation' in user_audio_text:
                call.NikkiTranslation(user_audio_text[17:],driver)

            elif 'weather in' in user_audio_text:
                call.NikkiSay('ok boss')
                mn = user_audio_text.find('in')
                cloud = user_audio_text[mn+3:].lower()
                call.NikkiWeather(cloud) 

            elif 'open insta' in user_audio_text or "open Instagram" in user_audio_text:
                res = user_audio_text.find('Prem')
                if user_audio_text[res:res+4] == 'Prem':
                    user_name = 'click_theworld1'
                    password = 'prem@123'
                    call.NikkiInsta(user_name,password,driver)
                user_name = input('enter your userName :')
                password = input('enter the password :')
                call.NikkiInsta(user_name,password,driver)

            elif 'what are you doing' in user_audio_text :
                call.NikkiSay("i'm still learning new things ")
                call.NikkiFeelTalk() 

            elif 'feeling boring' in user_audio_text:
                call.NikkiFeelTalk()

            elif 'reading time' in user_audio_text or ('read' in user_audio_text and ('book' in user_audio_text or 'books' in user_audio_text)):
                call.NikkiSay('which book you want boss')
                res = call.NikkiVoiceSource()
                call.Nikkibook(res,driver)
            elif 'how are you' in user_audio_text or 'how Nikki' in user_audio_text:
                call.NikkiSay("i'm doing great what about you")

            elif 'time in' in user_audio_text  :
                mn = user_audio_text.find('in')
                timeL = user_audio_text[mn+3:].lower()
                call.NikkiTime(timeL)

            elif 'who is' in user_audio_text:
                call.NikkiSay('ok Boss')
                call.NikkiWhoIs(user_audio_text[6:])

            elif 'JavaScript book' in user_audio_text or 'JS book' in user_audio_text:
                call.NikkiopenJavascript(driver)
            
            elif 'any joke' in user_audio_text or 'tell' in user_audio_text and 'joke' in user_audio_text:
                r = random.randrange(0,len(joke_nik)-1)
                call.NikkiSay(f'ok boss {joke_nik[r],joke_nik[r]}')

            elif 'new movie' in user_audio_text and 'movie time' in user_audio_text:
                call.NikkiSearch('https://ww16.ibomma.bar/telugu-movies/',driver)

            elif "news today" in user_audio_text or 'today news' in user_audio_text:
                call.NikkiSay('ok boss wait for a second')
                call.NikkiNewstoday()


            elif 'I love you' in user_audio_text or 'I love you' in user_audio_text :
                call.NikkiSay('hoo thank you i love you too Boss')

            elif 'feeling boring' in user_audio_text:
                call.NikkiFeelTalk()

            elif 'bhai' in user_audio_text or 'exit' in user_audio_text or 'bye' in user_audio_text:
                call.NikkiSay(' bye boss i miss you ')
                break 

            elif 'mute' in user_audio_text or 'Unmute' in user_audio_text or 'sleep' in user_audio_text:
                eng.setProperty('volume', 0)
                call.NikkiMute(user_audio_text)

            elif ('set up' in user_audio_text or 'set' in user_audio_text and ('Browser' in user_audio_text or 'browser' in user_audio_text ))or 'new browser' in user_audio_text:
                call.NikkiSay('wait boss setting the broser it will take few seconds')
                driver = webdriver.Chrome(executable_path="/home/navgurukul/Downloads/chromedriver-sel/chromedriver")
                driver.get('file:///home/navgurukul/Desktop/premlearn/nikki/front_nikki.html')

            elif 'close tab' in user_audio_text or 'close the tab' in user_audio_text:
                tabName = user_audio_text[user_audio_text.find('tab')+4:]
                call.NikkiCloseTab(tabName)

            elif 'mute' in user_audio_text or 'Unmute' in user_audio_text or 'sleep' in user_audio_text:
                call.NikkiMute(user_audio_text)

            else:
                call.NikkiSay('i am still learning ')

        elif user_audio_text == 'what is your name' or user_audio_text in 'your name':
            call.NikkiSay('hello my name is NIKKI by prem')

        elif 'Close Tab' in user_audio_text or 'close the tab' in user_audio_text or 'stop music' in user_audio_text:
            tabName = user_audio_text[user_audio_text.find('tab')+4:]
            call.NikkiCloseTab(tabName,user_audio_text,driver)

        elif 'how to use' in  user_audio_text or 'help' in user_audio_text:
            call.NikkiSay("you can ask first you need to say 'NIKKI' After 'Nikki play song' , news today, any joke, who is, time in ,open YouTube,open insta,weather ")
        
        elif 'mute' in user_audio_text or 'Unmute' in user_audio_text or 'sleep' in user_audio_text:
            call.NikkiMute(user_audio_text)

        elif ('set up' in user_audio_text or 'set' in user_audio_text and ('Browser' in user_audio_text or 'browser' in user_audio_text ))or 'new browser' in user_audio_text:
            call.NikkiSay('wait boss setting the broser it will take few seconds')
            driver = webdriver.Chrome(executable_path="/home/navgurukul/Downloads/chromedriver-sel/chromedriver")
            driver.get('file:///home/navgurukul/Desktop/premlearn/nikki/front_nikki.html')

        elif 'set account' in user_audio_text or 'set google' in user_audio_text:
            call.NikkiSetGoogle(driver,user_audio_text)
            
        else:
            call.NikkiSay('tell Nikki name and ask anything')
    except sr.UnknownValueError:                            # call back code 
            eng.say('Could not understand audio')
            eng.runAndWait()
            if error > 2:
                s = 0
                voices = eng.getProperty('voices')
                eng.setProperty('voice', 'english_rp+f3')
                eng.setProperty('volume',0)
                TrueFalse = True

                while TrueFalse :
                    try:   
                        error,TrueFalse = call.NikkiCallBack(error,TrueFalse)
                    except sr.UnknownValueError:
                        s+=1 

                        if s == 300:
                            call.NikkiSay('Hello boss i here to help you')
                            r = random.randrange(0,len(joke_nik)-1)
                            call.NikkiSay(joke_nik[r])   
                    except :
                        call.NikkiSay('oopes error boss')
                        pass

            else:
                error+=1

    except sr.RequestError:
        call.NikkiSay('network error check you wifi ')
        netError+=1
        print(netError)
        if netError > 8:
            s = 0
            voices = eng.getProperty('voices')
            eng.setProperty('voice', 'english_rp+f3')
            eng.setProperty('volume',0)
            TrueFalse = True

    except :
        call.NikkiSay('oopes MAIN ERROR boss')
