import os
import platform
import eel
from backend.auth import recoganize
from backend.auth.recoganize import AuthenticateFace
from backend.feature import *
from backend.command import *

eel.init("frontend")

playAssistantSound()

@eel.expose
def init():
    eel.hideLoader()
    speak("Welcome to Jarvis")
    speak("Ready for Face Authentication")
    flag = recoganize.AuthenticateFace()
    if flag ==1:
        speak("Face recognized successfully")
        eel.hideFaceAuth()
        eel.hideFaceAuthSuccess()
        speak("Welcome to Your Assistant")
        eel.hideStart()
        playAssistantSound()
    else:
        speak("Face not recognized. Please try again")

url = "http://localhost:8000/index.html"
system_os = platform.system()

if system_os == "Windows":
    os.system(f'start msedge.exe --app="{url}"')  # Or use start chrome if preferred
elif system_os == "Darwin":  # macOS
    os.system(f'open -a "Google Chrome" "{url}"')  # Uses Chrome if installed
else:
    os.system(f'xdg-open "{url}"')  # Linux or others

eel.start("index.html", mode=None, host="localhost", block=True)
