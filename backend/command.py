import pyttsx3
import speech_recognition as sr

#Initialize the Text-to-speech engine
def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    print(voices)
    engine.setProperty('voice', voices[2].id)
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', 174) 

    speak("Hello, I am Sharlok. How can I help you today?")

def techcommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source,10,8)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-US')
        print(f"User said:{query}\n")
    except Exception as e:
        print(f"Error:{str(e)}\n")
        return None
    
    return query.lower()

text1 =techcommand()

speak(text1)