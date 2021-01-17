import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if "assistant" in command.lower():
                command = command.replace("assistant", "")
                print(command)
    except:
        pass
    return command

def run_assistant():
    command = take_command()
    if "play" in command:
        song = command.replace("play", "")
        talk(f"playing {song}")
        pywhatkit.playonyt(song)
    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        talk(f"Current time is {time}")
    if "date" in command:
        date = datetime.datetime.now().strftime("%D")
        talk(f"Current date is {date}")
    if "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 3)
        talk(info)
    if "search" in command:
        topic = command.replace("search", "")
        engine.say("searching")
        pywhatkit.search(topic)
    else:
        talk("please say that again")

while True:
    run_assistant()
