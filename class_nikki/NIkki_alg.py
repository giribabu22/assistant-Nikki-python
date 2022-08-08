# from http.server import executable
# from os import system
import time
import speech_recognition as sr
import requests,random
import pyttsx3
import function_nikki as call

joke_nik = [['I invented a new word!Plagiarism!],[Did you hear about the mathematician who’s afraid of negative numbers?He’ll stop at nothing to avoid them.'],['Why do we tell actors to “break a leg?”Because every play has a cast. Here are some dark jokes to check out if you have a morbid sense of humor.'],['Helvetica and Times New Roman walk into a bar.“Get out of here!” shouts the bartender. “We don’t serve your type.”],[Yesterday I saw a guy spill all his Scrabble letters on the road. I asked him, “What’s the word on the street?”Once my dog ate all the Scrabble tiles. For days he kept leaving little messages around the house. Don’t miss these hilarious egg puns that will absolutely crack you up.'],['Knock! Knock! Who’s there? Control Freak. Con… OK, now you say, “Control Freak who?”' ],['Hear about the new restaurant called Karma? There’s no menu: You get what you deserve.'],['A woman in labor suddenly shouted, “Shouldn’t! Wouldn’t! Couldn’t! Didn’t! Can’t!”“Don’t worry,” said the doc. “Those are just contractions.”'],['A bear walks into a bar and says, “Give me a whiskey and … cola.” “Why the big pause?” asks the bartender. The bear shrugged. “I’m not sure; I was born with them.”'],['Did you hear about the actor who fell through the floorboards?He was just going through a stage.'],['Did you hear about the claustrophobic astronaut? He just needed a little space.'],['Why don’t scientists trust atoms? Because they make up everything.'],['Why did the chicken go to the séance?To get to the other side. Check out these other “why did the chicken cross the road?” jokes for more laughs.'],['Where are average things manufactured?The satisfactory.'],['How do you drown a hipster? Throw him in the mainstream.'],['What sits at the bottom of the sea and twitches?A nervous wreck.'],['What does a nosy pepper do? Gets jalapeño business!'],['How does Moses make tea? He brews.'],['Why can’t you explain puns to kleptomaniacs?They always take things literally.'],['How do you keep a bagel from getting away?Put lox on it.'],['A man tells his doctor, “Doc, help me. I’m addicted to Twitter!”The doctor replies, “Sorry, I don’t follow you …”']]

eng = pyttsx3.init()
voices = eng.getProperty('voices')
eng.setProperty('voice', 'english_rp+f2') 
eng.runAndWait()
eng.setProperty('volume', 4.0)


print(''' 
    hello this is Nikki assistant 
    i will answer your questions ?
''')

eng.say('hello this is Nikki assistant. i am ready to help you')
eng.runAndWait()
error = 1

while True:
  try:  
    user_audio_text = call.nikki.NikkiVoiceSource(sr,eng)
    print("You said :" + user_audio_text)

    if 'Nikki' in user_audio_text:
        
        if 'back' in user_audio_text or 'exit' in user_audio_text:
            print('<<<<<<<<<>> Bye boss<<>>>>>>>>>>')
            eng.say(' Bye boss ')
            eng.runAndWait()
            break

        elif 'hi' in user_audio_text or 'hello' in user_audio_text:
            call.timeFun()
            call.nikki.NikkiWork()

        elif 'what about you' in user_audio_text or 'what about you' in user_audio_text:
            eng.say("i'm Nikki i born in june 13 2022 developed by Prem kumar he is very creative person because he created me i respect him ")
            eng.runAndWait()

        elif 'p***' in user_audio_text or 'sex videos' in user_audio_text :
            eng.say('what the hell you want man fuck your self >>>>>>>>')
            pass 

        elif 'blog' in user_audio_text or 'blog app' in user_audio_text:
            call.nikki.NIkkiblog() 

        elif 'open insta' in user_audio_text or "open Instagram" in user_audio_text:
            eng.say('ok boss ! wait i am opening Instagram ')
            eng.runAndWait()
            res = user_audio_text.find('Prem')
            if user_audio_text[res:res+4] == 'Prem':
                print('running')
                user_name = 'click_theworld1'
                password = 'prem@123'
                call.nikki.NikkiInsta(user_name,password,)
            user_name = input('enter your userName :')
            password = input('enter the password :')
            call.nikki.NikkiInsta(user_name,password,)

        elif 'what are you doing' in user_audio_text :
            print("i'm still learning new things !")
            eng.say("i'm still learning new things ")
            # call.nikki.NikkiBoring() 

        # elif 'feeling boring' in user_audio_text:
            # call.nikki.NikkiBoring()

        elif 'how are you' in user_audio_text or 'how Nikki' in user_audio_text:
            print("i'm doing great what about you : ")
            eng.say("i'm doing great what about you")
            eng.runAndWait()

        elif 'play song' in user_audio_text or 'play songs in YouTube music'  in user_audio_text or 'play music' in user_audio_text :
            eng.say('ok boss ! wait i am opening youtube music ')
            eng.runAndWait()
            if 'play songs in YouTube music' in user_audio_text:
                f = user_audio_text.find('music')+5
                song = user_audio_text[f:]
            else:
                l = user_audio_text.split()
                song = l[3:]
            call.nikki.NikkiPlaySong(song,)

        elif 'open YouTube' in user_audio_text or 'YouTube' in  user_audio_text:
            eng.say('ok boss ! wait i am opening YouTube')
            eng.runAndWait()
            value_ = user_audio_text.find('YouTube')
            search_ = user_audio_text[value_+8:]
            eng.say(f'ok boss finding{search_}')
            eng.runAndWait()
            call.nikki.NikkiYoutube(search_,)

        elif 'time in' in user_audio_text  :
            mn = user_audio_text.find('in')
            timeL = user_audio_text[mn+3:].lower()
            call.nikki.NikkiTime(timeL)

        elif 'search' in user_audio_text or 'find' in user_audio_text or 'research' in user_audio_text:
            eng.say('ok boss i am opening google for you')
            eng.runAndWait()
            call.nikki.NikkiSearch(user_audio_text,)

        elif 'who is' in user_audio_text:
            eng.say('ok boss')
            eng.runAndWait()
            call.nikki.NikkiWhoIs(user_audio_text[6:])

        elif 'any joke' in user_audio_text or 'tell' in user_audio_text and 'joke' in user_audio_text:
            r = random.randrange(0,len(joke_nik)-1)
            eng.say('ok boss')
            eng.runAndWait()
            eng.say(joke_nik[r])
            eng.runAndWait()

        elif "news today" in user_audio_text or 'today news' in user_audio_text:
            call.nikki.NikkiNewstoday()

        elif 'I love you' in user_audio_text or 'I love you' in user_audio_text :
            eng.say('hoo thank you i love you too')
            eng.runAndWait()

        elif 'wh' in user_audio_text:
            print('i am still learning--')
            eng.say('i am still learning --')
            eng.runAndWait()
        else:pass

    elif 'go to sleep' in user_audio_text:
        r.recognize_google(audio)

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
        except :
            print('hoho ')
            eng.say('hoohohoo')
            eng.runAndWait()
            pass
    else:
      error+=1

  except sr.RequestError:
      print("Could not request results")
      pass

  except (error):
    print(error,'hoho ')
    eng.say('hoohohoo')
    eng.runAndWait()
    pass