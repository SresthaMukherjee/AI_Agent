# import pyttsx3
# import speech_recognition as sr
# import eel

# def speak(text):
#     text = str(text)
#     engine = pyttsx3.init('sapi5')
#     voices = engine.getProperty('voices')
#     # print(voices)
#     engine.setProperty('voice', voices[0].id)
#     eel.DisplayMessage(text)
#     engine.say(text)
#     engine.runAndWait()
#     engine.setProperty('rate', 174)

# def takecommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("I'm listening...")
#         eel.DisplayMessage("I'm listening...")
#         r.pause_threshold = 1
#         r.adjust_for_ambient_noise(source)
#         audio = r.listen(source, 10, 8)

#     try:
#         print("Recognizing...")
#         eel.DisplayMessage("Recognizing...")
#         query = r.recognize_google(audio, language='en-US')
#         print(f"User said: {query}\n")
#         eel.DisplayMessage(query)
#         speak(query)
        
#     except Exception as e:
#         print(f"Error: {str(e)}\n")
#         return None

#     return query.lower()
# @eel.expose
# def takeAllCommands(message=None):
#         try:
#             query = takecommand() 
#             print(query)
#             if "open" in query:
#                 from backend.feature import openCommand
#                 openCommand(query)
            
#             elif "send message" in query or "call" in query or "video call" in query:
#                 print("hello")
#                 from backend.feature import findContact, whatsApp
#                 flag=""
#                 Phone, name = findContact(query)
#                 if(Phone!=0):
#                     # speak("Which mode you want to use whatsapp or mobile")
#                     # preferance=takecommand()
#                     # print(preferance)
#                     if "send message" in query:
#                         #if "send message" in query or "send sms" in query:
#                         flag= 'message'
#                         speak("what message to send")
#                         query = takecommand()
#                             #sendMessage (message, Phone, name)
#                     elif "call" in query: 
#                         flag='call'
#                              #makeCall (name, Phone)
#                     else:
#                            # speak("please try again")
#                         flag='video call'
#                     whatsApp(Phone,query,flag,name)
#                     # elif "whatsapp" in preferance:
#                     #     message=""
#                     #     if "send message" in query:
#                     #         message = 'message'
#                     #         speak("what message to send")
#                     #         query=takecommand()

#                     #     elif "phone call" in query:
#                     #         message = 'call'
#                     #     else:
#                     #         message = 'video call'

#                     #whatsApp(Phone, query, message, name)
#             elif "youtube" in query:
#                 from backend.feature import playYoutube
#                 playYoutube(query)
            
#             else:
#                 print("I am not sure what to do...")   
#         except:
#             print("An error occurred...")

# #text1 =takecommand()
# #speak(text1) #return twice
#         eel.ShowHood() 

# # @eel.expose
# # def takeAllCommands(message=None):
# #     if message is None:
# #         query = takecommand()  # If no message is passed, listen for voice input
# #         if not query:
# #             return  # Exit if no query is received
# #         print(query)
# #         eel.senderText(query)
# #     else:
# #         query = message  # If there's a message, use it
# #         print(f"Message received: {query}")
# #         eel.senderText(query)
    
# #     try:
# #         if query:
# #             if "open" in query:
# #                 from backend.feature import openCommand
# #                 openCommand(query)
# #             elif "send message" in query or "call" in query or "video call" in query:
# #                 from backend.feature import findContact, whatsApp
# #                 flag = ""
# #                 Phone, name = findContact(query)
# #                 if Phone != 0:
# #                     if "send message" in query:
# #                         flag = 'message'
# #                         speak("What message to send?")
# #                         query = takecommand()  # Ask for the message text
# #                     elif "call" in query:
# #                         flag = 'call'
# #                     else:
# #                         flag = 'video call'
# #                     whatsApp(Phone, query, flag, name)
# #             elif "on youtube" in query:
# #                 from backend.feature import PlayYoutube
# #                 PlayYoutube(query)
# #             else:
# #                 from backend.feature import chatBot
# #                 chatBot(query)
# #         else:
# #             speak("No command was given.")
# #     except Exception as e:
# #         print(f"An error occurred: {e}")
# #         speak("Sorry, something went wrong.")
    
# #     eel.ShowHood()

import platform
import pyttsx3
import speech_recognition as sr
import eel

# Determine platform and initialize TTS engine accordingly
system_os = platform.system()
if system_os == "Windows":
    engine = pyttsx3.init("sapi5")
elif system_os == "Darwin":
    engine = pyttsx3.init("nsss")
else:
    engine = pyttsx3.init()  # fallback for Linux

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 174)

def speak(text):
    text = str(text)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening...")
        eel.DisplayMessage("I'm listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=8)

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        return query.lower()

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

@eel.expose
def takeAllCommands(message=None):
    try:
        query = message.lower() if message else takecommand()

        if not query:
            speak("I didn't catch that.")
            return

        print(f"Processing: {query}")
        eel.senderText(query)

        if "open" in query:
            from backend.feature import openCommand
            openCommand(query)

        elif "send message" in query or "call" in query or "video call" in query:
            from backend.feature import findContact, whatsApp
            flag = ""

            Phone, name = findContact(query)
            if Phone != 0:
                if "send message" in query:
                    flag = 'message'
                    speak("What message do you want to send?")
                    msg = takecommand()
                elif "call" in query:
                    flag = 'call'
                    msg = ''
                else:
                    flag = 'video call'
                    msg = ''
                whatsApp(Phone, msg, flag, name)

        elif "youtube" in query:
            from backend.feature import playYoutube
            playYoutube(query)

        else:
            speak("I am not sure what to do with that command.")

    except Exception as e:
        print(f"An error occurred: {e}")
        speak("Sorry, something went wrong.")

    eel.ShowHood()
