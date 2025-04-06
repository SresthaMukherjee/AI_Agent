import os
import eel
import platform
from backend.feature import *
from backend.command import *

def start():
    eel.init("frontend")

    url = "http://localhost:8000/index.html"
    system_os = platform.system()

    if system_os == "Windows":
        os.system(f'start msedge.exe --app="{url}"')  # Or use 'start chrome' if Chrome is default
    elif system_os == "Darwin":  # macOS
        os.system(f'open "{url}"')
    else:  # Linux or others
        os.system(f'xdg-open "{url}"')  # Works in most Linux distros

    playAssistantSound()

    eel.start("index.html", mode=None, host="localhost", block=True)
