import service.alg as alg
import os
# import dbus
# import dbus.mainloop.glib
from sub_task.NikkiSay import NikkiSay


from dotenv import load_dotenv
import speech_recognition as sr
from selenium import webdriver
import random
import json
    

flag = 'unmute'
joke_nik = [['I invented a new word!Plagiarism!],[Did you hear about the mathematician who’s afraid of negative numbers?He’ll stop at nothing to avoid them.'], ['Why do we tell actors to “break a leg?”Because every play has a cast. Here are some dark jokes to check out if you have a morbid sense of humor.'], ['Helvetica and Times New Roman walk into a bar.“Get out of here!” shouts the bartender. “We don’t serve your type.”],[Yesterday I saw a guy spill all his Scrabble letters on the road. I asked him, “What’s the word on the street?”Once my dog ate all the Scrabble tiles. For days he kept leaving little messages around the house. Don’t miss these hilarious egg puns that will absolutely crack you up.'], ['Knock! Knock! Who’s there? Control Freak. Con… OK, now you say, “Control Freak who?”'], ['Hear about the new restaurant called Karma? There’s no menu: You get what you deserve.'], ['A woman in labor suddenly shouted, “Shouldn’t! Wouldn’t! Couldn’t! Didn’t! Can’t!”“Don’t worry,” said the doc. “Those are just contractions.”'], [
    'A bear walks into a bar and says, “Give me a whiskey and … cola.” “Why the big pause?” asks the bartender. The bear shrugged. “I’m not sure; I was born with them.”'], ['Did you hear about the actor who fell through the floorboards?He was just going through a stage.'], ['Did you hear about the claustrophobic astronaut? He just needed a little space.'], ['Why don’t scientists trust atoms? Because they make up everything.'], ['Why did the chicken go to the séance?To get to the other side. Check out these other “why did the chicken cross the road?” jokes for more laughs.'], ['Where are average things manufactured?The satisfactory.'], ['How do you drown a hipster? Throw him in the mainstream.'], ['What sits at the bottom of the sea and twitches?A nervous wreck.'], ['What does a nosy pepper do? Gets jalapeño business!'], ['How does Moses make tea? He brews.'], ['Why can’t you explain puns to kleptomaniacs?They always take things literally.'], ['How do you keep a bagel from getting away?Put lox on it.'], ['A man tells his doctor, “Doc, help me. I’m addicted to Twitter!”The doctor replies, “Sorry, I don’t follow you …”']]
last_call = None
c = 0
load_dotenv()
error = 1
netError = 0
meeringMk = 0
meetingEng = 0
main_path = os.path.abspath(os.getenv('main_path'))+'/'

try:
    NikkiSay('wait boss setting the browser it will take few seconds')
    chrome_profile_directory =	"/home/prem/.config/BraveSoftware/Brave-Browser/Default"
    chrome_driver_path = main_path + 'chromedriver-sel/chromedriver'
    brave_binary_location = '/usr/bin/brave-browser'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = brave_binary_location
    chrome_options.add_argument('--remote-debugging-port=9000')
    chrome_options.add_argument("--user-data-dir=" + chrome_profile_directory)

    webdriver.chrome.driver = chrome_driver_path

    driver = webdriver.Chrome(options=chrome_options)
    call = alg.Service(driver, main_path)  # object create
    tabNames =   call.tabNamecheck()
    if 'nikki' not in tabNames:
        call.driver.get(f'file://{main_path}views/front_nikki.html')
        call.NikkiSetGoogle('l')


except Exception as e:
    e = str(e)
    if 'delimiter' in e or 'Extra data' in e:
        with open(f'{main_path}Manage_file/time_for_meeting.json', 'w') as f:
            f.write(json.dumps({}, indent=3))
    NikkiSay(f'oopes something wrong in first set up function. boss')

def reCallFun(error):
    if error > 2:
        TrueFalse = True
        while TrueFalse:
            try:
                error, TrueFalse = call.NikkiCallBack(error, TrueFalse)
            except:
                TrueFalse = False
        return error
    else:
        error += 1
        return error


t = 0
while True:
    try:
        call.NikkiAutoJoinMeeting()
        user_audio_text = call.NikkiQuickVoice()
        t = 0
        netError = 3
        if user_audio_text == None:
            TrueFalse = True
            error = reCallFun(error)
        call.NikkiCondition(user_audio_text)

    except sr.UnknownValueError:
        sentences = [
            "I couldn't comprehend the audio.",
            "The audio was unintelligible to me.",
            "I didn't understand what the audio was saying.",
            "The audio was unclear and difficult to grasp.",
            "I had trouble deciphering the audio.",
            "The audio was beyond my comprehension.",
            "I couldn't make sense of the audio.",
            "I struggled to comprehend the audio.",
            "The audio was incomprehensible to me.",
            "I was unable to understand what the audio was conveying."
        ]

        random_sentence = random.choice(sentences)                              # call back code
        call.NikkiSay(random_sentence)
        error = reCallFun(error)

    except sr.RequestError:
        call.NikkiSay('Boss, Network error check you wifi.')
        netError += 1
        if netError > 6:
            s = 0
            TrueFalse = True

    except Exception as e:
        try:
            e = str(e)
            if 'delimiter' in e or 'Extra data' in e:
                with open(f'{main_path}Manage_file/time_for_meeting.json', 'w') as f:
                    f.write(json.dumps({}, indent=3))

            elif 'unknown' in e or 'call' in e and t <= 10:
                t += 1
                if t >= 5:
                    break
                NikkiSay(
                    'Unexpected somthing wrong dont worry Boss. i  am set it. wait boss setting the browser it will take few seconds')
                chrome_options = webdriver.ChromeOptions()
                chrome_options.binary_location = '/usr/bin/brave-browser'
                chrome_options.add_argument('--remote-debugging-port=9000')
                chrome_options.add_argument("--user-data-dir=" + chrome_profile_directory)

                driver = webdriver.Chrome(
                main_path+'chromedriver-sel/chromedriver', chrome_options=chrome_options)
                call = alg.Service(driver, main_path)  # object create
                tabNames =   call.tabNamecheck()
                if 'nikki' not in tabNames:
                    call.driver.get(f'file://{main_path}views/front_nikki.html')
                    call.NikkiSetGoogle('l')

                try:
                    call.NikkiCondition(user_audio_text)
                except:
                    pass

        except Exception as e:
            NikkiSay("don't do anything, Boss")