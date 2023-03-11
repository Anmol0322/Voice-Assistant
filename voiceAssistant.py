import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import sys
import webbrowser
import os
import smtplib

# it helps to understand charmap
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am your speech assistant    Sir. Please tell me how may I help you")

def takeCommand():
    # It takes microphones input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # 1 sec pause is possible
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com, 587')
    server.ehlo()
    server.starttls()
    server.login('myemail@gmail.com', 'mypassword')
    server.sendmail('myemail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            # print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com/")

        elif 'play music' in query:
            music_dr = 'D:\\Songs\\'
            songs = os.listdir(music_dr)
            # print(songs)
            os.startfile(os.path.join(music_dr, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'email to ananya' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ananyakadbe012@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")

            except Exception as e:
                # print(e)
                speak("Sorry my friend. I'm not able to send this email at the moment")
        
        elif 'shutdown' in query:
            print("Shutting down myself")
            sys.exit()