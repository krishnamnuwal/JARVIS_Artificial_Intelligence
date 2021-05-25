
from unittest import result
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import subprocess

engine=pyttsx3.init('sapi5')

# print(engine)
voices=engine.getProperty('voices')
# print(voices[0].id)

engine.setProperty('voice',voices[0].id)

###To use email function there is need to turn on the less secure app access 'on'
###otherwise email will not be sent 
###https://support.google.com/accounts/answer/6010255?hl=en#zippy=%2Cif-less-secure-app-access-is-off-for-your-account%2Cif-less-secure-app-access-is-on-for-your-account
        ##Through this link you can turn it on 
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('write your email id', 'write your email id password')
    server.sendmail('write your email id', to, content)
    server.close()

def speak(audio):
  engine.say(audio)
  engine.runAndWait() #Without this command, speech will not be audible to us.


def wishMe():
  hour=int(datetime.datetime.now().hour)
  if hour>=0 and hour<12:
      speak("Good Morning sir")

  elif hour>=12 and hour<18:
      speak("Good Afternoon sir")

  else:
      speak('Good Evening Sir')
      # speak(hour)
      # speak('pm')

  speak("I am Jarvis your virtual artificial intelligence! Please tell me how could I help you")

def takeCommand():
  #It Takes microphone input from users and returns string output

  r=sr.Recognizer()
  with sr.Microphone() as source:
    print('Listening...')
   # r.pause_threshold=2
    r.energy_threshold=200
    audio = r.listen(source)
  try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

  except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
  return query
  
if __name__ == "__main__":
    wishMe()
    while True:
      query=takeCommand().lower()

      

      if 'wikipedia' in query:
        speak('searching wikipedia...')
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
      elif 'introduce' in query:
        speak('Now me to introduce myself I am jarvis the virtual artificial intelligence ,designed by Krishnam Nuwal I am here to assist you with a variety of tasks as best I can .24 hours a day seven days a week importing preferences from home interface systems are now fully operational')

      elif 'open youtube' in query:
        speak('opening youtube')
        webbrowser.register('chrome',None)
        webbrowser.open('https://www.youtube.com')

      elif 'open google' in query:
        speak('opening google')
        webbrowser.open('https://www.google.com')

      elif 'open github' in query:
        speak('opening github')
        webbrowser.open('https://www.github.com')

      elif 'open white hat' in query:
        speak('opening whitehatjr')
        webbrowser.open('https://code.whitehatjr.com')

      elif 'play music' in query:
        speak('playing music')
        music_dir='E:\music'
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,random.choice(songs)))

      elif 'the time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir,the time is {strTime}")

      elif 'open visual studio code' in query:
        speak('opening visual studio code')
        codePath = "C:\\Users\\shree\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

      elif 'open sublime' in query:
        speak('opening sublime')
        limePath="C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
        os.startfile(limePath)

      elif 'open telegram' in query:
        speak('opening telegram')
        telPath="C:\\Users\\shree\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
        os.startfile(telPath)

      elif 'open brave' in query:
        speak('opening brave')
        brPath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        os.startfile(brPath)
      
      elif 'open chrome' in query:
        speak('opening chrome')
        crPath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(crPath)
      
      elif 'open d' in query:
        speak('opening drive d')
        dPath='D://'
        os.startfile(dPath)
      
      elif 'open e' in query:
        speak('opening drive E')
        ePath = 'E://'
        os.startfile(ePath)

      elif 'open c drive' in query:
        speak('opening drive C')
        cPath = 'C://'
        os.startfile(cPath)

      elif 'send email to krishnam' in query:
         try:
                speak("What should I say?")
                content = takeCommand()
                to = "write the email address to whom you want to send the mail"
                sendEmail(to, content)
                speak("Email has been sent!")
         except Exception as e:
                print(e)
                speak("Sorry Sir,I'm unable to send email")  
      
   
      
      elif 'search' in query:
        query=query.replace("search","")
        webbrowser.register('chrome', None)
        speak(f"searching {query}")
        webbrowser.open(query)
      
      elif "log off" in query or "sign out" in query or "shut down" in query:
          speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
          subprocess.call(["shutdown", "/l"])
      elif 'quit' in query or 'stop' in query or 'bye' in query:
        exit()
