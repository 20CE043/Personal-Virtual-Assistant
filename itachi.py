
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb



voice=pyttsx3.init()


def speak(audio):
    voice.say(audio)
    voice.runAndWait()

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
    time()
    date()

    hour= datetime.datetime.now().hour

    if(hour>=6 and hour<12):
        speak("Good Morning ma'am")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon ma'am")
    elif(hour>=18 and hour<24):
        speak("Good Evening ma'am")
    else:
        speak("Good Night ma'am")
    
    speak("itachi at your service. please tell me how can i help you today?")

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio, language='en-US')
        print(query)
    except Exception as e:
        print(e)
        print("please can you say that again....")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gamil.com',587)
    server.ehlo()
    server.starttls()
    server.login('username@gmail.com','password')
    server.sendmail('username@gmail.com',to,content)
    server.close()

# wishme()
# TakeCommand()
if __name__ == '__main__':
   # wishme()

    while True:
        query=TakeCommand().lower() #all command are taken in lowercase

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query=query.replace('wikipedia',' ')
            result=wikipedia.summary(query,sentences=5)
            speak("According to Wikipedia...")
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak('what should i say?')
                content=TakeCommand()
                
                speak("who is the reciever?")
                reciever=input("Eneter reciever's email adrees ")
                to=reciever
                sendEmail(to,content)
                speak(content)
                speak("Email has been send")

            except Exception as e:
                print(e)
                speak(e)
                speak("sorry,unable to send your Email...")
        
        elif 'search in chrome' in query:
            speak("what you wanna search?")
            chromepath="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"

            finds = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(finds+'.com') 

                


                


    
    
    

