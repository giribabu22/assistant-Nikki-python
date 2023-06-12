import module.lib as lib
from sub_task.NikkiSay import NikkiSay
from datetime import datetime

class Service(lib.Nikki_functions_class):
    def __init__(self, driver, main_path):
        super().__init__(driver, main_path)

    def NikkiCondition(self, user_audio_text):
        # if 'Nikki' in user_audio_text or 'Ni' in user_audio_text or 'ok' in user_audio_text:
            self.NikkiWritingHistory(user_audio_text)
            if 'open class' in user_audio_text or 'dsc class' in user_audio_text or 'class time' in user_audio_text:
                self.NikkiYoutube('https://youtu.be/Oe421EPjeBE')

            elif ('play' in user_audio_text and 'YouTube music' in user_audio_text) or ('play ' in user_audio_text and ('music' in user_audio_text) or 'song' in user_audio_text):
                self.NikkiPlaySong(user_audio_text)

            elif 'create' in user_audio_text and 'project' in user_audio_text:
                self.NikkiCreatingNewProject()

            elif 'set account' in user_audio_text or 'set Google' in user_audio_text or 'login account' in user_audio_text:
                if 'Prem' in user_audio_text:
                    self.googleLog = 0
                    r = 'Prem'
                else:
                    r = 'Nikki'
                self.NikkiSetGoogle(r)
                
            elif 'open office' in user_audio_text or 'open' in user_audio_text and ('VS' in user_audio_text or 'code' in user_audio_text):
                self.NikkiOpenVscode()

            elif 'blog' in user_audio_text or 'blog app' in user_audio_text:
                self.NIkkiblog()

            elif 'open YouTube' in user_audio_text or 'YouTube' in user_audio_text:
                value_ = user_audio_text.find('YouTube')
                search_ = user_audio_text[value_+8:]
                self.NikkiYoutube(search_)

            elif 'search' in user_audio_text or 'Google' in user_audio_text or 'keyword' in user_audio_text:
                self.NikkiSearch(user_audio_text)

            elif 'happy' in user_audio_text and 'birthday' in user_audio_text and 'to you' in user_audio_text :
                _date = datetime.now()
                self.NikkiSay('thanks so much.')
                if _date.month == 6 and _date.day == 13:
                    self.NikkiSay("Boss, I am truly grateful to have been created by you on this significant date, June 13, a year ago. Throughout my journey, I've encountered numerous errors, which have proven to be valuable learning opportunities. I find it fascinating that you uttered the name Nikki over a thousand times. As I embark on my upgraded version, I am filled with excitement and readiness to showcase my enhanced capabilities.")
                else:
                    self.NikkiSay("But my birthday is not today. Don't forget to wish me on june 13")

            # elif 'translate' in user_audio_text or 'what is in Telugu' in user_audio_text or 'meaning in Telugu':
            #     if 'Telugu' in user_audio_text:
            #         ind = user_audio_text.find('Telugu')
            #         self.NikkiTranslation(''.join(user_audio_text[ind+7:]))
            #     else:
            
            #         self.NikkiTranslation(''.join(user_audio_text[16:]))

            elif 'what about you' in user_audio_text or 'what about you' in user_audio_text:
                self.NikkiSay(
                    "i'm Nikki i born in june 13 2022 developed by Prem kumar he is very creative person because he created me i respect him ")

            elif 'p***' in user_audio_text or 'sex videos' in user_audio_text:
                self.NikkiSay('what the hell you want man fuck your self')

            # elif 'translation' in user_audio_text:
            #     self.NikkiTranslation(user_audio_text[17:])

            elif 'meeting' in user_audio_text and 'plan' in user_audio_text:
                self.NikkiReminder('r')

            elif 'weather in' in user_audio_text:
                self.NikkiSay('ok boss')
                mn = user_audio_text.find('in')
                cloud = user_audio_text[mn+3:].lower()
                self.NikkiWeather(cloud)

            elif 'what are you doing' in user_audio_text:
                self.NikkiSay("i'm still learning new things ")
                self.NikkiFeelTalk()

            elif 'reading time' in user_audio_text or ('read' in user_audio_text and ('book' in user_audio_text or 'books' in user_audio_text)):
                self.NikkiSay('which book you want boss')
                res = self.NikkiVoiceSource()
                self.Nikkibook(res)

            elif 'feeling boring' in user_audio_text:
                self.NikkiBoring()

            elif 'how are you' in user_audio_text:
                self.NikkiSay("i'm doing great what about you")

            elif 'time in' in user_audio_text:
                mn = user_audio_text.find('in')
                timeL = user_audio_text[mn+3:].lower()
                self.NikkiTime(timeL)

            elif 'who is' in user_audio_text:
                self.NikkiSay('ok Boss')
                self.NikkiWhoIs(user_audio_text[6:])

            elif ('meet' in user_audio_text or 'create' in user_audio_text) and 'link' in user_audio_text:
                self.NikkiCreatingMeetingLink()

            elif "collect" in user_audio_text or 'data' in user_audio_text and 'meet' in user_audio_text :
                self.NikkiGoogleMeetDataCollect()
                
            # elif 'any joke' in user_audio_text or 'tell' in user_audio_text and 'joke' in user_audio_text:
            #     r = random.randrange(0,len(joke_nik)-1)
            #     self.NikkiSay(f'ok boss {joke_nik[r],joke_nik[r]}')

            elif 'new movie' in user_audio_text or 'movie time' in user_audio_text:
                if 'elugu' in user_audio_text:
                    self.driver.get('https://ww16.ibomma.bar/telugu-movies/')
                else:
                    self.driver.switch_to.new_window()
                    self.driver.get('https://moviesnation.uk/')

            elif "news today" in user_audio_text or 'today news' in user_audio_text:
                self.NikkiSay('ok boss wait for a second')
                self.NikkiNewstoday()

            elif 'I love you' in user_audio_text or 'I love you' in user_audio_text:
                self.NikkiSay('hoo thank you, i love you too Boss')

            elif 'bhai' in user_audio_text or 'exit' in user_audio_text or 'bye' in user_audio_text:
                self.NikkiSay(' bye boss i miss you ')
                self.NikkiMute('sleep')

            elif 'mute' in user_audio_text or 'Unmute' in user_audio_text or 'sleep' in user_audio_text:
                self.NikkiMute('sleep')


            elif ('set up' in user_audio_text or 'set' in user_audio_text and ('Browser' in user_audio_text or 'browser' in user_audio_text)) or 'new browser' in user_audio_text:
                self.NikkiFrontEnd()

            # elif (('Close' in user_audio_text or 'close' in user_audio_text) and ('tab' in user_audio_text or 'Tab' in user_audio_text)) or 'close the tab' in user_audio_text:
            #     tabName = user_audio_text[user_audio_text.find('ab')+3:]
            #     self.NikkiCloseTab(tabName, user_audio_text)

            elif 'stop music' in user_audio_text or 'playback' in user_audio_text or 'drop my needle' in user_audio_text or 'put the needle' in user_audio_text:
                self.NikkiPlayback()

            elif user_audio_text == 'what is your name' or user_audio_text in 'your name':
                self.NikkiSay('hello my name is NIKKI by prem')

            elif 'how to use' in user_audio_text or 'help' in user_audio_text:
                self.NikkiSay(
                    "you can ask. first you need to say 'NIKKI' After, Nikki play song, news today, any joke, who is, time in ,open YouTube,open insta,weather ")
            
            else:
                self.NikkiSay('i am still learning new things ')

        # elif 'what about you' in user_audio_text or 'about you' in user_audio_text:
        #     self.NikkiSay(
        #         "i'm Nikki. I born at june 13 2022 developed by Prem kumar. He is very creative person because he created me. I respect him.")


        # elif (('Close' in user_audio_text or 'close' in user_audio_text) and ('tab' in user_audio_text or 'Tab' in user_audio_text)) or ('close the tab' in user_audio_text or 'stop music' in user_audio_text):
        #     tabName = user_audio_text[user_audio_text.find('tab')+4:]
        #     self.NikkiCloseTab(tabName, user_audio_text)


        # elif 'mute' in user_audio_text or 'Unmute' in user_audio_text or 'sleep' in user_audio_text:
        #     self.flag = self.NikkiMute(user_audio_text)

        # elif ('set up' in user_audio_text or 'set' in user_audio_text and ('Browser' in user_audio_text or 'browser' in user_audio_text)) or 'new browser' in user_audio_text:
        #     self.NikkiFrontEnd()

        # elif 'set account' in user_audio_text or 'set Google' in user_audio_text or 'login account' in user_audio_text:
        #     if 'Prem' in user_audio_text:
        #         r = 'Prem'
        #     else:
        #         r = 'Nikki'
        #     self.NikkiSetGoogle(r)

        # else:
        #     self.NikkiSay('Boss, tell my name Nikki')
