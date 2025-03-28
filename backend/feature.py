# import playsound as playsound
# import eel


# @eel.expose

# def playAssistantSound():
#     music_dir="C:\Users\HP\AI_Agent\frontend\assets\audio\frontend_assets_audio_start_sound.mp3"
#     playsound.playsound(music_dir) 

import os
import re
import eel
import pywhatkit as kit
import pygame
from backend.command import speak
from backend.config import ASSISTANT_NAME

#Initialize pygame mixer
pygame.mixer.init()

#Define the function to play sound
@eel.expose

def playAssistantSound ():
    sound_file = r"C:\Users\sukan\AI_Agent\frontend\assets\audio\frontend_assets_audio_start_sound.mp3"
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def openCommand(query):
    query=query.replace(ASSISTANT_NAME,"")
    query=query.replace("open","")
    query.lower()

    if query!="":
        speak("opening"+query)
        os.system('start'+query)
    else:
        speak("I'm sorry, I couldn't understand your command.")

def playYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing"+search_term+"on YouTube")
    kit.playonyt(search_term)
def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern,command,re.IGNORECASE)
    return match.group(1) if match else None