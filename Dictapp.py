import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep
from assistant import speak

# Simple app commands (must be in system PATH)
dictapp = {
    "Setting": "Settings",
    "brave": "Brave",
    "commandprompt": "cmd",
    "file manager": "explorer",
    "word": "winword",
    "excel": "excel",
    "chrome": "chrome",
    "vscode": "code",
    "powerpoint": "powerpnt"
}

def openappweb(query):
    speak("Please wait a moment")
    query = query.replace("open", "").replace("Genos", "").replace("launch", "").strip().lower()
    
    if ".com" in query or ".co.in" in query or ".org" in query:
        webbrowser.open(f"https://www.{query}")
        return
    
    for app in dictapp:
        if app in query:
            os.system(f"start {dictapp[app]}")
            return

    speak("I can't seem to find that app you are asking .")

def closeappweb(query):
    speak("Closing, sir")

    if "tab" in query:
        num_tabs = int(query.split()[0]) if query.split()[0].isdigit() else 1
        for _ in range(num_tabs):
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
        speak("All tabs are closed")
    else:
        found = False
        for app in dictapp:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
                speak(f"{app} has been closed")
                found = True
                break
        
        if not found:
            speak("I dont think you have that  application  installed")
