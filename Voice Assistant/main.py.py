import pyttsx3
import datetime
import  wikipedia
import speech_recognition as sr
import webbrowser
import os
print("Tejas Assistant VERSION 1.0")


engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon")
        speak("Good Afternoon!")

    else:
        print("Good Evening")
        speak("Good Evening!")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print(e)
        print("Say the again Plzzzz...")
        return "None"
    return query

def PlayGame():
    print("Ok play Game from here:")
    print("\nSnake\nPac-Man\nAtari Breakout\nZerg Rush\nT-rex Dash\nGoogle Gravity\nDoodle Cricket\nFlappy Bird"
        "\nGoogle Word Coach")


wishme()

while True:
    query = takecommand().lower()

    #Wikipedia

    if 'what is' in query or "wikipedia" in query:
        speak("searching Wikipedia...")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        print("According to Wikipedia...")
        speak("According to Wikipedia...")
        print(results)
        speak(results)
        print("\nFor more information opening Wikipedia page...")
        speak("For more information opening Wikipedia page")
        webbrowser.open(f"https://en.wikipedia.org/wiki/{query}")
        break


    #Assistant questions

    elif 'who are you' in query:
        print("I am Assistant Made By Tejas! Please tell me how may I help you")
        speak("I am Assistant Made By Tejas! Please tell me how may I help you")

    elif 'thank you' in query:
        print("Welcome friend...")
        speak("Welcome friend")

    #Opening Website
    elif 'open youtube' in query:
        print("Opening Youtube...")
        speak("Opening Youtube")
        webbrowser.open("www.youtube.com")
        break

    elif 'open google' in query:
        print("Opening Google...")
        speak("Opening Google")
        webbrowser.open("www.Google.com")
        break


    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Sir the current time is {strTime}")
        speak(f"Sir the current time is {strTime}")


    elif 'translate' in query:
        print("Ok, translate the words from here:")
        speak("Ok, translate the words from here")
        google_translate = str(input("Enter the word jiska aapko meaning chahiye hai:"))
        webbrowser.open(f"https://translate.google.co.in/#view=home&op=translate&sl=en&tl=hi&text={google_translate}")
        break


    elif 'game' in query:
        PlayGame()

    elif 'snake' in query:
        print("Opening Google Snake Game...")
        speak("Opening Google Snake Game...")
        webbrowser.open("https://www.google.com/search?q=play+snake")
        break

    elif 'pacman' in query:
        print("Opening Pac-Man Game...")
        speak("Opening Pac-Man Game...")
        webbrowser.open("https://www.google.com/search?q=play+pacman+doodle")
        break

    elif 'atari breakout' in query:
        print("Opening Atari Breakout game...")
        speak("Opening Atari Breakout game")
        webbrowser.open("https://elgoog.im/breakout/")
        break

    elif 'zerg rush' in query:
        print("Opening Zerg Rush game...")
        speak("Opening Zerg Rush game")
        webbrowser.open("https://elgoog.im/zergrush/")
        break

    elif 't rex dash' in query:
        print("Opening T-Rex Dash game...")
        speak("Opening T-Rex Dash game")
        webbrowser.open("https://elgoog.im/t-rex/")
        break

    elif 'google gravity' in query:
        print("Opening Googke Gravity game...")
        speak("Opening Googke Gravity game")
        webbrowser.open("https://mrdoob.com/projects/chromeexperiments/google-gravity/")
        break

    elif 'doodle cricket' in query:
        print("Opening Doodle Cricket game...")
        speak("Opening Doodle Cricket game")
        webbrowser.open("https://doodlecricket.github.io/#/")
        break

    elif 'flappy bird' in query:
        print("Opening Flappy Bird game...")
        speak("Opening Flappy Bird game")
        webbrowser.open("https://flappybird.io/")
        break

    elif 'about' in query:
        print("\tAbout:")
        print("Made by Tejas\nTejas Assistant\nVersion 1.O")


    elif 'quit' in query:
        speak("Okkk Quitting Voice Assistant")
        print("Okkk Quitting Voice Assistant!!")
        break













