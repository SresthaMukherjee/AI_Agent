import os
import platform
import eel
import datetime

from backend.auth import recoganize
from backend.auth.recoganize import AuthenticateFace
from backend.feature import *
from backend.command import *

# Initialize the frontend directory for Eel
eel.init("frontend")
# ✅ Play assistant start sound
playAssistantSound()

@eel.expose
def init():
    eel.hideLoader()
    speak("welcome to Sherlock")

    speak("Ready for Face Authentication")
    is_authenticated = recoganize.AuthenticateFace()

    if is_authenticated == 1:
        speak("Face recognized successfully")
        eel.hideFaceAuth()
        eel.hideFaceAuthSuccess()
        speak("Welcome to your assistant")  # 🔁 This is where you might be hearing "Welcome to Jarvis"
        eel.hideStart()
        playAssistantSound()
    else:
        speak("Face not recognized. Please try again")

# ✅ Set browser startup URL
url = "http://localhost:8000/index.html"
system_os = platform.system()

# ✅ Open in default browser depending on OS
if system_os == "Windows":
    os.system(f'start msedge.exe --app="{url}"')  # ✅ You can change to chrome.exe if needed
elif system_os == "Darwin":
    os.system(f'open -a "Google Chrome" "{url}"')
else:
    os.system(f'xdg-open "{url}"')


# ✅ Start the Eel web interface
eel.start("index.html", mode=None, host="localhost", block=True)