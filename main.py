import os
import platform
import eel
import datetime
from backend.auth import recoganize
from backend.auth.recoganize import AuthenticateFace
from backend.feature import *
from backend.command import *

eel.init("frontend")

def get_greeting():
    """Return appropriate greeting based on time of day"""
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "Good Morning"
    elif 12 <= hour < 17:
        return "Good Afternoon"
    else:
        return "Good Evening"

playAssistantSound()

@eel.expose
def init():
    eel.hideLoader()
    speak("Welcome to Sherlock")
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
