import time
import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import os
import pyautogui
import datetime
import keyboard
import pyjokes


assistant= pyttsx3.init('sapi5')
voices=assistant.getProperty('voices')
# print(voices)
assistant.setProperty('voice',voices[0].id)
assistant.setProperty('rate',180)

def speak(audio):
    # print("hello ma'am, im jarvis at your servis..")
    assistant.say(audio)
    print(audio)
    # print()
    assistant.runAndWait()
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")# for 24 hour time schedule use %H and for 12 hour time schedule use %I
    speak("The current time is ")
    speak(Time)

def date():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().day
    speak("The current date is ")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Himani!")

    hour= datetime.datetime.now().hour

    if(hour>=6 and hour<12):
        speak("Good Morning ma'am")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon ma'am")
    elif(hour>=18 and hour<24):
        speak("Good Evening ma'am")
    else:
        speak("Good Night ma'am")
    
    speak("jarvis at your service ma'am.")

def takeCommand():
    command=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        command.pause_threshold = 1
        audio=command.listen(source)

    try:
        print('recognizing...')
        query=command.recognize_google(audio,language='en-in')
        print("you said : ",query)

    except Exception as e :
        print('sorry , say that again')
        return "none"
    
    return query.lower()

def playMusic():
    speak("which song do you wanna play...")
    musicName=takeCommand()
    if 'abhi to party' in musicName:
        os.startfile("C:\\Users\\HP\Music\\Abhi Toh Party.mp3")
    elif 'fakira' in musicName:
        os.startfile("C:\\Users\\HP\\Music\\Fakira.mp3")
    else:
        pywhatkit.playonyt(musicName)
    speak("your song has been started, enjoy ma'am")

def openApps():
    speak("which app or file do you wanna open")
    task=takeCommand()
    if 'pycharm' in task:
        os.startfile("C:\\Users\\Public\\Desktop\\PyCharm Community Edition 2021.3.1.lnk")
        speak(" done ma'am")
    if 'vs code' in task:
        os.startfile("C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk")
        speak(" done ma'am")
    if 'wireshark' in task:
        os.startfile("C:\\Users\\Public\\Desktop\\Wireshark.lnk")
        speak(" done ma'am")
    if 'command promt' in task:
        os.startfile("C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk")
        speak(" done ma'am")
    if 'control panel' in task:
        os.startfile("C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk")
        speak(" done ma'am")
    if 'anydisk' in task:
        os.startfile("C:\\Users\\Public\\Desktop\\AnyDesk.lnk")
        speak(" done ma'am")
    if 'whatsapp' in task:
        os.startfile("C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp\\WhatsApp.lnk")
        speak(" done ma'am")
    if 'code blocks' in task:
        os.startfile("C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\CodeBlocks\\CodeBlocks.lnk")
        speak(" done ma'am")
    if 'google chrome' in task:
        os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
        speak(" done ma'am")

# def dict():
#     speak("Activated Dictionary mode !")
#     speak("tell me the problem")
#     prob=takeCommand()

#     if 'meaning' in prob:
#         prob= prob.replace("what is the ","")
#         prob= prob.replace("jarvis")
#         prob=prob.replce("of")


def taskExe():

    wishme()
    while True:
        
        query = takeCommand()
        if 'hello ' in query:
            speak("hello... ma'am")
            speak("your persnoal AI assistan")
            speak("hoe can i help you")
        
        elif 'how are you' in query:
            speak("I'm fine ma'am")
            speak("what about you?")
        
        elif 'time' in query:
                time()
        
        elif 'date' in query:
            date()
        
        elif 'you need a break' in query:
            speak("ok! ma'am you can call me any time..." )
            break
        
        elif 'youtube search 'in query:
            speak("ok ma'am ")
            query=query.replace("jarvis","")
            query=query.replace("youtube search","")
            web="https://www.youtube.com/results?search_query=" + query 
            webbrowser.open(web)
            speak("done ma'am")  
        
        elif 'google search'in query:
            try:
                speak("this is what i found")
                query=query.replace("jarvis","")
                query=query.replace("google search","")
                pywhatkit.search(query)
                speak("done ma'am")
            except Exception as e:
                print(e)
        
        elif 'website search' in query:
            speak("ok ! ma'am ,launching")
            query=query.replace("jarvis","")
            query=query.replace("website search","")
            web1=query.replace("open","")
            web2='http://www.' + web1 + '.com '
            webbrowser.open(web2)
            speak("launched !")
        
        elif 'launch website' in query:
            speak("what's the name of website that tu wanna launch")
            webname=takeCommand()
            web='http://www.'+ webname + '.com'
            webbrowser.open(web)
            speak("done ma'am")
        
        elif "open my college websit" in query:
            speak("opening...")
            webbrowser.open('https://www.charusat.ac.in/')
            speak("done ma'am...")
        
        elif "open facebook" in query:
            speak("opening...")
            webbrowser.open('https://www.facebook.com/')
            speak("done ma'am...")
        
        elif "open instagram" in query:
            speak("opening...")
            webbrowser.open('https://www.instagram.com/')
            speak("done ma'am...")
        
        elif 'open maps' in query:
            speak("opening...")
            webbrowser.open('https://www.google.com/maps/@20.9911557,72.9784777,13z')
            speak("done ma'am...")
        
        elif 'open youtube' in query:
            speak("opening...")
            webbrowser.open('https://www.youtube.com/')
            speak("done ma'am...")
             
        elif 'wikipedia' in query:
            speak("Searching...")
            query=query.replace('wikipedia',' ')
            result=wikipedia.summary(query,sentences=3)
            speak("According to Wikipedia...")
            print(result)
            speak(result)
        
        elif 'play music' in query:
            playMusic()

        elif 'take screenshot' in query:
            speak(" ma'am please tell me the name of your screenshort ")
            ssName=takeCommand()
            ssName1=ssName + ".png"
            path1='C:\\Users\\HP\\Pictures\\screenshort\\'+ssName1
            ss=pyautogui.screenshot()
            ss.save(path1)
            os.startfile("C:\\Users\\HP\\Pictures\\screenshort")
            speak("done ma'am... here your screenshort")
        
        elif 'open app' in query:  
            openApps()
        
        #    
        
        elif 'pause' or 'play' in query:
            keyboard.press('space bar')
            speak("done ma'am...")
        elif 'restart' in query:
            keyboard.press('0')
            speak("done ma'am...")
        elif 'mute' in query:
            keyboard.press('m')
            speak("done ma'am...")
        elif 'skip' in query:
            keyboard.press('l')
            speak("done ma'am...")
        elif 'back' in query:
            keyboard.press('j')
            speak("done ma'am...")
        elif 'full screen' in query:
            keyboard.press('f')
            speak("done ma'am...")
        elif 'next video' in query:
            keyboard.press('shift + n')
            speak("done ma'am...")
        elif 'previous video' in query:
            keyboard.press('shift + p')
            speak("done ma'am...")
        elif 'turn on caption' or 'turn off caption' in query:
            keyboard.press('c')
            speak("done ma'am...")
        elif 'film mode' in query:
            keyboard.press('t')
            speak("done ma'am...")
        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')
            speak("done ma'am...")
        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')
            speak("done ma'am...")
        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')
            speak("done ma'am...")
        elif 'open history' in query:
            keyboard.press_and_release('ctrl + h')
            speak("done ma'am...")
        elif 'show downloads' in query:
            keyboard.press_and_release('ctrl + j')
            speak("done ma'am...")
        elif 'open task manager' in query:
            keyboard.press_and_release('shift + esc')
            speak("done ma'am...")
        elif 'open developer tool' in query:
            keyboard.press_and_release('shift + ctrl + j')
            speak("done ma'am...")
        elif 'clear browsing data' in query:
            keyboard.press_and_release('ctrl + shift + delete')
            speak("done ma'am...")
        elif 'open help center' in query:
            keyboard.press_and_release('f1')
            speak("done ma'am...")
        elif 'make it bookmark' or 'remove bookmark' in query:
            keyboard.press_and_release('ctrl + shift +b')
            speak("done ma'am...")
        elif 'open incognito mode' in query:
            keyboard.press_and_release('ctrl + shift +n')
            speak("done ma'am...")
        elif 'reopen last 10 tabs that i closed ' in query:
            keyboard.press_and_release('ctrl + shift +t')
            speak("done ma'am...")
        elif 'jokes' in query:
            joke=pyjokes.get_joke()
            speak(joke)
        elif 'repeat my word' in query:
            speak('which word or sentence you wanna repeat')
            word=takeCommand()
            speak(' you said :',word)
taskExe()