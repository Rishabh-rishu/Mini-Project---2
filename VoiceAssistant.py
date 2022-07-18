import pyttsx3 
import datetime
import webbrowser
import smtplib
import keyboard
import os
import wikipedia
import speech_recognition as sr
from pynput.mouse import Button , Controller



m = Controller()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!!!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon!!!!")   

    else:
        speak("Good Evening!!!!!")  

    speak("I am Infinity Sir. Please tell me how may I help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print("User said: %s\n"%query)
        if 'how are you' not in query and 'tell me about yourself' not in query and "sing for me" not in query and 'I love you' not in query and 'good job infinity':
            speak(query)

    except Exception as e:   
        speak("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('anandgodara395@gmail.com','aradhaya@007')
    server.sendmail('anandgodara395@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia for' in query:
            speak('Searching Wikipedia...')
            query = query.split(" ")
            location = query[2:]
            location=' '.join(location)
            webbrowser.open('https://en.wikipedia.org/wiki/'+ location)
            text = wikipedia.summary(query)
            print(text)
            speak(text)

        elif 'open youtube' in query:
            query = query.split(" ")
            c=query[1:]
            location=' '.join(c)
            webbrowser.open('https://www.youtube.com/')
            

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open gla website' in query:
            webbrowser.open("www.gla.ac.in")
        elif 'how are you' in query:
            speak('i am fine what can i do  for you')
        elif 'tell me about yourself' in query:
            speak('i am infinity your personal virtual assistant created to help you')
        elif 'play ' in query:
            query=query.split(" ")
            location = query[1:]
            location=' '.join(location)
            webbrowser.open("https://www.youtube.com/results?search_query=" + location)
            m.position = (395,306)
            for _ in range(10000):
                for i in range(10000):
                    pass
            m.press(Button.left)
            m.release(Button.left)
            #m.position = (855,618)
            for _ in range(1000):
                for i in range(1000):
                    pass
            keyboard.press_and_release('f')
        
            
        elif "where is" in query:
            query = query.split(" ")
            location = query[2:]
            location=' '.join(location)
            speak("Hold on Sir, I will show you where " + location + " is.")
            webbrowser.open('https://www.google.com/maps/place/'+ location)
            m.position = (318,98)
            for _ in range(10000):
                for i in range(10000):
                    pass
            m.press(Button.left)
            m.release(Button.left)
        elif "record audio" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Say something!")
                audio = r.listen(source)

        # Speech recognition using Google Speech Recognition
            data = ""
            try:
            # Uses the default API key
            # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                data = r.recognize_google(audio)
                speak("i recorded: " + data)
                speak("do you want to save this audio")
                with sr.Microphone() as s:
                    ad=r.listen(s)
                y=r.recognize_google(ad)
                if "yes" in y:
                    speak("file has been successfully saved")
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

        elif 'open playlist' in query:
            music_dir = "C:\\Users\\HP\\Music\\Playlists"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Sir, the time is %s"%strTime)
        elif 'date' in query:
            strDate = datetime.datetime.now().strftime("%d:%B:%Y")    
            speak("Sir, the date is %s"%strDate)
        elif 'open code' in query:
            codePath = "C:\\Users\\This PC\\Desktop\\rex.py"
            os.startfile(codePath)

        elif 'email to anand' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "anand.godara_cs19@gla.ac.in"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")
        elif 'email to deevansh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "deevansh.katare_cs19@gla.ac.in"    
                sendEmail(to, content)
                speak("Email has been sent!")
                continue
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")
        elif 'email to rishabh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rishabh.tripathi_cs19@gla.ac.in"    
                sendEmail(to, content)
                speak("Email has been sent!")
                continue
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")  
        elif 'email to ritik' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ritik.varshney_cs19@gla.ac.in"    
                sendEmail(to, content)
                speak("Email has been sent!")
                continue
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")
        elif 'email to Farmanul sir' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "md.farmanul@gla.ac.in"    
                sendEmail(to, content)
                speak("Email has been sent!")
                continue
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")

        elif 'email to pratyush' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "pratyush.khare_cs18@gla.ac.in"    
                sendEmail(to, content)
                speak("Email has been sent!")
                continue
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")
        
        elif 'tell me about' in query:
            try:
                speak('this is what i found')
                query=query.split(" ")
                content=query[3:]
                webbrowser.open('https://www.google.com/search?q=' + str(*content))
            except Exception as e:
                speak("sorry")
        elif 'good job infinity' in query:
            speak('thank you sir')
        elif 'i love you' in query:
            speak('I am a Machine. Find another partner for you')
        elif "shutdown" in query:
            speak("do you wish to shutdown your computer")
            speak("press enter to shutdown!")
            os.system("shutdown /s /t 1")
        elif 'open word' in query:
            speak("opening Microsoft word")
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk')
        elif 'open excel' in query:
            speak("opening Microsoft Excel")
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk')
        elif 'open powerpoint' in query:
            speak("opening Microsoft powerpoint")
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk')
        else:
            try:
               if "none" not in query:
                    speak('this is what i found')
                    webbrowser.open('https://www.google.com/search?q=' + str(query))
            except Exception as e:
                speak("sorry")
    
        
    
       
