import os
import platform
import eel
from backend.feature import *
from backend.command import *

eel.init("frontend")

url = "http://localhost:8000/index.html"
system_os = platform.system()

if system_os == "Windows":
    os.system(f'start msedge.exe --app="{url}"')  # Or use start chrome if preferred
elif system_os == "Darwin":  # macOS
    os.system(f'open -a "Google Chrome" "{url}"')  # Uses Chrome if installed
else:
    os.system(f'xdg-open "{url}"')  # Linux or others

playAssistantSound()

eel.start("index.html", mode=None, host="localhost", block=True)
