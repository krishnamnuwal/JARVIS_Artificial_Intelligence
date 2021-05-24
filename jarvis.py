
from unittest import result
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
engine=pyttsx3.init('sapi5')

# print(engine)
voices=engine.getProperty('voices')
# print(voices[0].id)

engine.setProperty('voice',voices[1].id)




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

  speak("I am Jarvis .Please tell me how may I help you")

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
        c=webbrowser.get('chrome')
        c.open("youtube.com")
    