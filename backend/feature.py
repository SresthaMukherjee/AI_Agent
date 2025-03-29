# import playsound as playsound
# import eel


# @eel.expose

# def playAssistantSound():
#     music_dir="C:\Users\HP\AI_Agent\frontend\assets\audio\frontend_assets_audio_start_sound.mp3"
#     playsound.playsound(music_dir) 

import os
import re
import webbrowser
import eel
import pywhatkit as kit
import pygame
from backend.command import speak
from backend.config import ASSISTANT_NAME
import sqlite3

conn=sqlite3.connect("sherlock.db")
cursor=conn.cursor()

#Initialize pygame mixer
pygame.mixer.init()

#Define the function to play sound
@eel.expose

def playAssistantSound ():
    sound_file = r"C:\Users\NEW\AI_Agent\frontend\assets\audio\frontend_assets_audio_start_sound.mp3"
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def openCommand(query):
    query=query.replace(ASSISTANT_NAME,"")
    query=query.replace("open","")
    query.lower()

    app_name=query.strip()
    if app_name!="":
        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN(?)',(app_name,))
            results=cursor.fetchall()
            
            if len(results)!=0:
                speak("Opening"+query)
                os.startfile(results[0][0])

            elif len(results)==0:
                cursor.execute(
                   'SELECT url FROM web_command WHERE name IN(?)',(app_name,))
                results=cursor.fetchall()

                if len(results)!=0:
                    speak("Opening"+query)
                    webbrowser.open(results[0][0])
                else:
                    speak("Opening"+query)
                    try:
                        os.system('start'+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")
#     if query!="":
#         speak("opening"+query)
#         os.system('start'+query)
#     else:
#         speak("I'm sorry, I couldn't understand your command.")

def playYoutube(query):
    search_term = query  # or some other logic to set search_term
    if search_term:
        speak("Playing " + search_term + " on YouTube")
    else:
        speak("Sorry, no search term was provided.")



# def playYoutube(query):
#     search_term = extract_yt_term(query)  # Extract search term properly
#     if search_term:
#         speak(f"Playing {search_term} on YouTube")
#         kit.playonyt(search_term)  # Open YouTube video
#     else:
#         speak("Sorry, I couldn't understand what to play on YouTube.")

def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern,command,re.IGNORECASE)
    return match.group(1) if match else None