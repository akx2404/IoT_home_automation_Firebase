import pyttsx3
import speech_recognition as sr
import random
import time
import os
import turtle
from firebase import firebase
import datetime
import serial
import time as t
import json

#connect to firebase db
my_url = 'https://home-automation2404-default-rtdb.firebaseio.com/'
fb = firebase.FirebaseApplication(my_url, None)


def main_page():
    window.clearscreen()
    window.bgpic('brain.GIF')
    window.title("Alpha bot")

    
text = turtle.Turtle()
text.color('yellow')
text.penup()
#text.hideturtle()
text.goto(-350, 50)
text.right(90)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
        newVoiceRate = 155
        engine.setProperty('rate',newVoiceRate)
        engine.say(audio)
        engine.runAndWait()

def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning Sir")
            text.write('Good Morning Sir', font=('Fixedsys',15,'bold'))
            text.forward(20)

        elif hour>=12 and hour<18:
            speak("Good afternoon sir")
            text.write('Good Afternoon Sir', font=('Fixedsys',15,'bold'))
            text.forward(20)
            
        else:
            speak("Good evening sir")
            text.write('Good Evening Sir', font=('Fixedsys',15,'bold'))
            text.forward(20)
            
        speak("What can I do for you?")
        turtle.forward(15)
        text.write('What can I do for you?', font=('Fixedsys',15,'bold'))
        time.sleep(1)


def takeCommand():

        r = sr.Recognizer()
        with sr.Microphone() as source:
            text.clear()
            text.write('Listening....', font=('Fixedsys',15,'bold'))
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            text.clear()
            text.write('Recognizing...', font=('Fixedsys',15,'bold'))
            text.clear()
            query = r.recognize_google(audio, language='en-in')
            text.write(f"you said: {query}\n", font=('Fixedsys',15,'bold'))
            time.sleep(2)
            #print(f"User said: {query}\n")

        except Exception as e:
            #print(e)
            return "None"

        return query
        

if __name__=="__main__":
    #create window
    window = turtle.Screen()
    window.setup(800,300)
    main_page()
    time.sleep(1)
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wejh' in query:
            a = 0

        elif 'on' in query:
            speak("Got it sir, Switching on the light")
            result = fb.patch(my_url + '', {'data': "1"})


        elif 'off' in query:
            speak("Got it sir, Switching off the light")
            result = fb.patch(my_url + '', {'data': "0"})

        if "exit" in query:
            speak("Bye sir")
            time.sleep(1)
            turtle.bye()
            break

