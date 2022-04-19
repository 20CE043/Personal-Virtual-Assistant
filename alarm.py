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
import datetime
from playsound import playsound


assistant= pyttsx3.init('sapi5')
voices=assistant.getProperty('voices')
# print(voices)
assistant.setProperty('voice',voices[0].id)
assistant.setProperty('rate',180)

def speak(audio):
    assistant.say(audio)
    print(audio)
    assistant.runAndWait()

def takeCommand():
    command=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        command.adjust_for_ambient_noise(source)
        command.pause_threshold = 1
        audio=command.listen(source)
        

    try:
        print('recognizing...')
        query=command.recognize_google(audio,language='en-in')
        print("you said : ",query)

    except Exception as e :
        print('sorry , say that again')
        return takeCommand()
    
    return query.lower()



def taskexs():
    while True:
        query=takeCommand()

        if 'alarm' in query:
            speak("enter the time : ")
            time=input()

            while True:
                timeal=datetime.datetime.now()
                now=timeal.strftime("%I:%M:%S")
                
                if now == time:
                    speak("time to wake up ma'am....")
                    rigtone="Abhi_Toh_Party.mp3"
                    os.system(rigtone)
                elif now>time:
                    break
        
                
taskexs()