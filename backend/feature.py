import playsound as playsound
import eel


@eel.expose

def playAssistantSound():
    music_dir="C:\\Users\\NEW\\AI_Agent\\frontend\\assets\\audio\\frontend_assets_audio_start_sound.mp3"
    playsound.playsound(music_dir)