# import pyttsx3
# import speech_recognition as sr

# #Initialize the Text-to-speech engine
# def speak(text):
#     engine = pyttsx3.init('sapi5')
#     voices = engine.getProperty('voices')
#     print(voices)
#     engine.setProperty('voice', voices[2].id)
#     engine.say(text)
#     engine.runAndWait()
#     engine.setProperty('rate', 174) 

#     speak("Hello, I am Sharlok. How can I help you today?")

# def techcommand():
#     r=sr.Recognizer()
#     with sr.Microphone() as source:
#         print("I'm listening...")
#         r.pause_threshold=1
#         r.adjust_for_ambient_noise(source)
#         audio=r.listen(source,10,8)
#     try:
#         print("Recognizing...")
#         query=r.recognize_google(audio,language='en-US')
#         print(f"User said:{query}\n")
#     except Exception as e:
#         print(f"Error:{str(e)}\n")
#         return None
    
#     return query.lower()

# text1 =techcommand()

# speak(text1)
import pyttsx3
import speech_recognition as sr

# Initialize Text-to-Speech engine
def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')

    # Print available voices for debugging
    for index, voice in enumerate(voices):
        print(f"Voice {index}: {voice.id}")

    # Use a valid voice index
    if len(voices) > 2:
        engine.setProperty('voice', voices[2].id)
    elif len(voices) > 1:
        engine.setProperty('voice', voices[1].id)
    else:
        engine.setProperty('voice', voices[0].id)

    engine.setProperty('rate', 174)  # Set speech rate before speaking
    engine.say(text)
    engine.runAndWait()

def techcommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=8)  # Avoids infinite listening
        except sr.WaitTimeoutError:
            print("Listening timeout, no input detected.")
            return None

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError:
        print("Could not request results, check your internet connection.")
    
    return None

# Get user command and speak response
text1 = techcommand()
if text1:
    speak(text1)
else:
    speak("I didn't catch that. Can you repeat?")
