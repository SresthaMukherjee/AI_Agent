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

# SQLite Connection
conn = sqlite3.connect("sherlock.db")
cursor = conn.cursor()

# Initialize pygame mixer
pygame.mixer.init()

@eel.expose
def playAssistantSound():
    sound_file = r"/Users/sresthamukherjee/AI_Agent/frontend/assets/audio/frontend_assets_audio_start_sound.mp3"
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "").replace("open", "").strip().lower()
    app_name = query

    if not app_name:
        return

    try:
        cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
        results = cursor.fetchall()

        if results:
            speak("Opening " + app_name)
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
                speak("Opening " + app_name)
                webbrowser.open(results[0][0])
            else:
                speak("Opening " + app_name)
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
    speak(f"Playing {search_term} on YouTube")
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
                print("Hotword detected")

                if platform.system() == "Windows":
                    pyautogui.keyDown("win")
                    pyautogui.press("j")
                    time.sleep(2)
                    pyautogui.keyUp("win")
                else:
                    # Placeholder for macOS/Linux shortcut handling
                    print("Triggering hotword action on non-Windows OS")

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
            speak('Contact not found')
            return 0, 0
    except:
        speak('Contact not found')
        return 0, 0

def whatsApp(Phone, message, flag, name):
    target_tab = {"message": 12, "call": 7, "video": 6}.get(flag, 6)
    jarvis_message = {
        "message": f"Message sent successfully to {name}",
        "call": f"Calling {name}",
        "video": f"Starting video call with {name}"
    }.get(flag, f"Interacting with {name}")

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
        speak(f"Error sending WhatsApp: {str(e)}")
