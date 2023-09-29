import pyttsx3

engine = pyttsx3.init()

def Speak(text):
    engine.say(text=text)
    engine.runAndWait()