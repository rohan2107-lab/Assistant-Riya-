import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("I am Riya sir. Please tell me how may I help you")

def takeCommand():
    # it takes microphone input and return string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User Said : {query}\n")

    except Exception as e:
        print(e)

        print("say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gamil.com',587)
    server.ehlo()
    server.starttls()
    server.login('rr7905860@gmail.com','psaaword******')
    server.sendmail('rr7905860@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for task
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Opening Youtube sir..")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\hp\\Music\\R. Music'
            songs = os.listdir(music_dir)
            #print(songs)
            speak("Playing Music sir..")
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to rohan' in query:
            try:
                speak("What should I say ?")
                content = takeCommand()
                to = "rohankumar@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir , I am not able to send this email.")

        elif 'open word' in query:
            wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            speak("Opening Word sir..")
            os.startfile(wordPath)

        elif 'open excel' in query:
            excelPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            speak("Opening Excel sir...")
            os.startfile(excelPath)

        elif 'tell me about yourself' in query:
            speak("Hello! I'm Riya, your personal  assistant. I’m here to help you with tasks on your laptop, whether it's organizing files, scheduling, or finding information.I can assist with a variety of tasks like managing your emails, setting up reminders, browsing the web, editing documents, and much more. I was created by ,Rohan, to help with everyday work on the laptop. He designed me to make your tasks simpler and more efficient.I’m powered by advanced algorithms that allow me to understand your commands and perform tasks based on your instructions. You can interact with me through voice.Just tell me what you need, and I’ll get it done.")

        elif 'stop the program' in query:
            speak("stoping program sir..")
            exit()

        