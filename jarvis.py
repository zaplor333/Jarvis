
import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import nltk
from nltk.chat.util import Chat, reflections
from gtts import gTTS
import json
from functions import *

with open("data.json", 'r') as f:
    data = json.load(f)




class Jarvis():
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.speak("Hello Sir!")

    def action(self, sentence):
        # first word
        for word1 in sentence.split(): 
            if word1 in data.keys(): # e.g. open, add
                #second word
                for word2 in sentence.split():
                    if word2 in data[word1].keys():
                        function = word1+'_'+word2
                        return eval(f"{function}()")

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio =self.recognizer.listen(source)
            return audio
    
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    
    
    def audio_to_text(self, audio):
        try:
            text = self.recognizer.recognize_google(audio) # , language="en-in"
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return None
        except sr.RequestError as e:
            print("Sorry, I couldn't request results from Google Speech Recognition service; {0}".format(e))
            return None
    
    def text_to_audio(self, text, lang='en'):
        return gTTS(text, lang)