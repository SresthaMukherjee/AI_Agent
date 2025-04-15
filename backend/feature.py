# import os
# from shlex import quote
# import struct
# import subprocess
# import time
# import webbrowser
# import eel
# import pvporcupine
# import pyaudio
# import pyautogui
# import pywhatkit as kit
# import pygame
# from backend.command import speak
# from backend.config import ASSISTANT_NAME
# import sqlite3
# from backend.helper import extract_yt_term, remove_words

# conn = sqlite3.connect("sherlock.db")
# cursor = conn.cursor()

# #Initialize pygame mixer
# pygame.mixer.init()

# #Define the function to play sound
# @eel.expose

# def playAssistantSound ():
#     sound_file = r"//Users//sresthamukherjee//AI_Agent//frontend//assets//audio//frontend_assets_audio_start_sound.mp3"
#     pygame.mixer.music.load(sound_file)
#     pygame.mixer.music.play()

# def openCommand(query):
#     query=query.replace(ASSISTANT_NAME,"")
#     query=query.replace("open","")
#     query.lower()
#     # if query!="":
#     #     speak("opening"+query)
#     #     os.system('start'+query)
#     # else:
#     #     speak("I'm sorry, I couldn't understand your command.")

#     app_name = query.strip()

#     if app_name != "":

#         try:
#             cursor.execute( 
#                 'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
#             results = cursor.fetchall()

#             if len(results) != 0:
#                 speak("Opening "+query)
#                 os.startfile(results[0][0])

#             elif len(results) == 0: 
#                 cursor.execute(
#                 'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
#                 results = cursor.fetchall()
                
#                 if len(results) != 0:
#                     speak("Opening "+query)
#                     webbrowser.open(results[0][0])

#                 else:
#                     speak("Opening "+query)
#                     try:
#                         os.system('start '+query)
#                     except:
#                         speak("not found")
#         except:
#             speak("some thing went wrong")

# def playYoutube(query):
#     search_term = extract_yt_term(query)
#     speak("Playing"+search_term+"on YouTube")
#     kit.playonyt(search_term)

# def hotword():
#     porcupine=None
#     paud=None
#     audio_stream=None
#     try:
       
#         # pre trained keywords    
#         porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) 
#         paud=pyaudio.PyAudio()
#         audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
#         # loop for streaming
#         while True:
#             keyword=audio_stream.read(porcupine.frame_length)
#             keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

#             # processing keyword comes from mic 
#             keyword_index=porcupine.process(keyword)

#             # checking first keyword detetcted for not
#             if keyword_index>=0:
#                 print("hotword detected")

#                 # pressing shorcut key win+j
#                 import pyautogui as autogui
#                 autogui.keyDown("win")
#                 autogui.press("j")
#                 time.sleep(2)
#                 autogui.keyUp("win")
                
#     except:
#         if porcupine is not None:
#             porcupine.delete()
#         if audio_stream is not None:
#             audio_stream.close()
#         if paud is not None:
#             paud.terminate()

# def findContact(query):
    
#     words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
#     query = remove_words(query, words_to_remove)

#     try:
#         query = query.strip().lower()
#         cursor.execute("SELECT Phone FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
#         results = cursor.fetchall()
#         print(results[0][0])
#         mobile_number_str = str(results[0][0])

#         if not mobile_number_str.startswith('+91'):
#             mobile_number_str = '+91' + mobile_number_str

#         return mobile_number_str, query
#     except:
#         speak('not exist in contacts')
#         return 0, 0
    
# def whatsApp(Phone, message, flag, name):
    

#     if flag == 'message':
#         target_tab = 12
#         jarvis_message = "message send successfully to "+name

#     elif flag == 'call':
#         target_tab = 7
#         message = ''
#         jarvis_message = "calling to "+name

#     else:
#         target_tab = 6
#         message = ''
#         jarvis_message = "staring video call with "+name
#     # Encode the message for URL
#     encoded_message = quote(message)
#     print(encoded_message)
#     # Construct the URL
#     whatsapp_url = f"whatsapp://send?phone={Phone}&text={encoded_message}"

#     # Construct the full command
#     full_command = f'start "" "{whatsapp_url}"'

#     # Open WhatsApp with the constructed URL using cmd.exe
#     subprocess.run(full_command, shell=True)
#     time.sleep(5)
#     subprocess.run(full_command, shell=True)
    
#     pyautogui.hotkey('ctrl', 'f')

#     for i in range(1, target_tab):
#         pyautogui.hotkey('tab')

#     pyautogui.hotkey('enter')
#     speak(jarvis_message)

import os
import struct
import subprocess
import time
import webbrowser
import platform
from shlex import quote

import eel
import pvporcupine
import pyaudio
import pyautogui
import pywhatkit as kit
import pygame
import sqlite3

from backend.command import speak
from backend.config import ASSISTANT_NAME
from backend.helper import extract_yt_term, remove_words

conn = sqlite3.connect("sherlock.db")
cursor = conn.cursor()

# Initialize pygame mixer
pygame.mixer.init()

# Define the function to play sound
@eel.expose
def playAssistantSound():
    sound_file = r"/Users/sresthamukherjee/AI_Agent/frontend/assets/audio/frontend_assets_audio_start_sound.mp3"
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "").replace("open", "").strip().lower()
    app_name = query

    if app_name:
        try:
            cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if results:
                speak("Opening " + query)
                path = results[0][0]
                if platform.system() == "Windows":
                    os.startfile(path)
                elif platform.system() == "Darwin":
                    os.system(f'open "{path}"')
                else:
                    os.system(f'xdg-open "{path}"')

            else:
                cursor.execute('SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()

                if results:
                    speak("Opening " + query)
                    webbrowser.open(results[0][0])
                else:
                    speak("Opening " + query)
                    if platform.system() == "Windows":
                        os.system(f'start {app_name}')
                    elif platform.system() == "Darwin":
                        os.system(f'open -a "{app_name}"')
                    else:
                        os.system(f'xdg-open "{app_name}"')

        except Exception as e:
            speak(f"Something went wrong: {str(e)}")

def playYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing " + search_term + " on YouTube")
    kit.playonyt(search_term)

def hotword():
    porcupine = None
    paud = None
    audio_stream = None

    try:
        porcupine = pvporcupine.create(keywords=["jarvis", "alexa"])
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(rate=porcupine.sample_rate, channels=1,
                                 format=pyaudio.paInt16, input=True,
                                 frames_per_buffer=porcupine.frame_length)

        while True:
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)
            keyword_index = porcupine.process(keyword)

            if keyword_index >= 0:
                print("hotword detected")

                if platform.system() == "Windows":
                    pyautogui.keyDown("win")
                    pyautogui.press("j")
                    time.sleep(2)
                    pyautogui.keyUp("win")
                else:
                    print("Hotword detected - implement macOS shortcut if needed")

    except Exception as e:
        print("Error in hotword detection:", e)
    finally:
        if porcupine:
            porcupine.delete()
        if audio_stream:
            audio_stream.close()
        if paud:
            paud.terminate()

def findContact(query):
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove).strip().lower()

    try:
        cursor.execute("SELECT Phone FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", 
                       ('%' + query + '%', query + '%'))
        results = cursor.fetchall()

        if results:
            mobile_number_str = str(results[0][0])
            if not mobile_number_str.startswith('+91'):
                mobile_number_str = '+91' + mobile_number_str
            return mobile_number_str, query
        else:
            speak('not exist in contacts')
            return 0, 0
    except:
        speak('not exist in contacts')
        return 0, 0

def whatsApp(Phone, message, flag, name):
    if flag == 'message':
        target_tab = 12
        jarvis_message = "message sent successfully to " + name
    elif flag == 'call':
        target_tab = 7
        message = ''
        jarvis_message = "calling " + name
    else:
        target_tab = 6
        message = ''
        jarvis_message = "starting video call with " + name

    encoded_message = quote(message)
    whatsapp_url = f"whatsapp://send?phone={Phone}&text={encoded_message}"

    try:
        if platform.system() == "Windows":
            full_command = f'start "" "{whatsapp_url}"'
            subprocess.run(full_command, shell=True)
            time.sleep(5)
            subprocess.run(full_command, shell=True)
        elif platform.system() == "Darwin":
            subprocess.run(["open", whatsapp_url])
        else:
            subprocess.run(["xdg-open", whatsapp_url])
        
        pyautogui.hotkey('ctrl', 'f')
        for _ in range(1, target_tab):
            pyautogui.hotkey('tab')
        pyautogui.hotkey('enter')
        speak(jarvis_message)

    except Exception as e:
        speak("Error sending WhatsApp: " + str(e))
