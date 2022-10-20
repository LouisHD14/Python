import pyttsx3



read = input("Schreibe was ausgegeben werden soll: ")
number = int(input("Wie oft soll es ausgegeben werden? "))



def tts():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(read)
    engine.runAndWait()



for i in range(number):
    tts()


