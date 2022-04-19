from fnmatch import translate
import time
from unittest import result
from jupyterlab_server import translator
from pyparsing import line
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
from playsound import playsound
from googletrans import Translator


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

def takeinhindi():
    
    command=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        command.adjust_for_ambient_noise(source)
        command.pause_threshold = 1
        audio=command.listen(source)
        

    try:
        print('recognizing...')
        query=command.recognize_google(audio,language='hi')
        print("you said : ",query)

    except Exception as e :
        print('sorry , say that again')
        return takeinhindi()
    
    return query.lower()

def trans():
     speak("speak something ")
     line=takeinhindi()
     trans=Translator()
     result = trans.translate(line)
     Text=result.text
     speak(Text)

def taskexs():
    while True:
        query=takeCommand()

        if "translator" in query:
            trans()

taskexs()