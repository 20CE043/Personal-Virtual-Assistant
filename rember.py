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

        if 'remember' in query:
            remm=query.replace('remember that',"")
            speak("you taold me to remember that : "+ remm)
            # remember=open('data.text','w')
            # remember.write(remm)
            # remember.close()
        elif 'do you remember something' in query:
            # remember=open('data.text','r')
            speak("you told me to remind you to ",remm)

taskexs()