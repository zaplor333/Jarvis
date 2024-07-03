
import os
import pyttsx3
import speech_recognition as sr
import webbrowser
from gtts import gTTS

def name():
    var = os.environ.get(name)
    return f"my name is {var}"
def open_cmd():
        os.system("start")
        return "command promt is opening..."
def open_youtube():
        webbrowser.open('https://www.youtube.com')
        return "youtube is opening..."
def open_notepad():
        os.system("notepad.exe") # for window users
        return "notepad is opening..."
def open_vscode():
        os.system("code.exe")
        return "vscode is opening..."
