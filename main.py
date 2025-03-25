import os
import eel
eel.init("frontend")
os.system('start msedge.exe --app="http://127.0.0.1:5500/frontend/index.html"')

  
eel.start("index.html",mode=None,host="localhost",block=True)

