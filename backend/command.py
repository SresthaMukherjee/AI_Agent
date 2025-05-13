import platform
import pyttsx3
import speech_recognition as sr
import eel

# Initialize TTS engine based on OS
system_os = platform.system()
if system_os == "Windows":
    try:
        engine = pyttsx3.init("sapi5")
    except Exception:
        print("sapi5 not available")
        engine = pyttsx3.init()    
elif system_os == "Darwin":
    engine = pyttsx3.init("nsss")
else:
    engine = pyttsx3.init()  # Linux or fallback

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 174)

# Speak function with eel display
def speak(text):
    text = str(text)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()
@eel.expose
# Speech recognition function
def takecommand():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("I'm listening...")
            eel.DisplayMessage("I'm listening...")
            recognizer.pause_threshold = 1
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=8)

        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        return query.lower()

    except sr.WaitTimeoutError:
        speak("I didn't hear anything.")
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
    except Exception as e:
        print(f"Error: {str(e)}")
        speak("An error occurred while listening.")

    return None

# Main command processing function
@eel.expose
def takeAllCommands(message=None):
    try:
        query = message.lower() if message else takecommand()
        if not query:
            speak("I didn't catch that.")
            return

        print(f"Processing: {query}")
        
        
        if "open" in query:
            from backend.feature import openCommand
            openCommand(query)

        elif "send message" in query or "video call" in query or "call" in query:
            from backend.feature import findContact, whatsApp
            flag = ""
            msg = ""

            Phone, name = findContact(query)
            if Phone != 0:
                if "send message" in query:
                    flag = "message"
                    speak("What message do you want to send?")
                    msg = takecommand()
                elif "video call" in query:
                    flag = "video"
                elif "call" in query:
                     flag = 'call'

                if flag == "message" and not msg:
                    speak("Message was not received. Cancelling.")
                    return

                whatsApp(Phone, msg, flag, name)

        elif "youtube" in query:
            from backend.feature import playYoutube
            playYoutube(query)

        else:
            from backend.feature import chatBot
            chatBot(query)

        # else:
        #     speak("I am not sure what to do with that command.")

    except Exception as e:
        print(f"An error occurred: {e}")
        speak("Sorry, something went wrong.")
    finally:
        eel.ShowHood()
