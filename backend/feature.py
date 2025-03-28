# import playsound as playsound
# import eel


# @eel.expose

# def playAssistantSound():
#     music_dir="C:\Users\HP\AI_Agent\frontend\assets\audio\frontend_assets_audio_start_sound.mp3"
#     playsound.playsound(music_dir) 

import eel
import pygame

#Initialize pygame mixer
pygame.mixer.init()

#Define the function to play sound
@eel.expose

def playAssistantSound ():
    sound_file = r"C:\Users\HP\AI_Agent\frontend\assets\audio\frontend_assets_audio_start_sound.mp3"
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()