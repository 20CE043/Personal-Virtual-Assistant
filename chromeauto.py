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

        if 'open chrome' in query:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk")
        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + W')
            speak("done ma'am...")
        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + T')
            speak("done ma'am...")
        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + N')
            speak("done ma'am...")
        elif 'open history' in query:
            keyboard.press_and_release('ctrl + H')
            speak("done ma'am...")
        elif 'show downloads' in query:
            keyboard.press_and_release('ctrl + J')
            speak("done ma'am...")
        elif 'open task manager' in query:
            keyboard.press_and_release('shift + esc')
            speak("done ma'am...")
        elif 'open developer tool' in query:
            keyboard.press_and_release('shift + ctrl + J')
            speak("done ma'am...")
        elif 'clear browsing data' in query:
            keyboard.press_and_release('ctrl + shift + delete')
            speak("done ma'am...")
        elif 'open help center' in query:
            keyboard.press_and_release('f1')
            speak("done ma'am...")
        elif 'make it bookmark' or 'remove bookmark' in query:
            keyboard.press_and_release('ctrl + shift +B')
            speak("done ma'am...")
        elif 'open incognito mode' in query:
            keyboard.press_and_release('ctrl + shift +N')
            speak("done ma'am...")
        elif 'reopen last 10 tabs that i closed ' in query:
            keyboard.press_and_release('ctrl + shift +T')
            speak("done ma'am...")
        
        
taskexs()

