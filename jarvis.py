
import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import nltk
from nltk.chat.util import Chat, reflections
from gtts import gTTS
from pairs import pairs

class ChatBot():
    def __init__(self):
        self.data = pairs

    def reply(self, query):
        chat = Chat(self.data, reflections)
        response = chat.respond(query)
        return response



class Action():
    def __init__(self, sentence):
        if "open youtube" in sentence:
            return self.open_youtube()
        elif "open notepad" in sentence:
            return self.open_notepad()
        else:
            response = self.chatbot(sentence)
            return response

    def chatbot(self, promt):
        # TODO: use openai api for get response
        chatbot = ChatBot()
        reply = chatbot.reply(promt)
        return reply
    
    def open_notepad(self):
        os.system("notepad.exe") # for window users
        return "notepad opening..."
    def open_youtube(self):
        webbrowser.open('https://www.youtube.com')
        return "youtube opening..."




class Jarvis(Action):
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.speak("Hello Sir!")

    def action(self, sentence):
        response = super().__init__(sentence)
        return response

    
    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio =self.recognizer.listen(source)
            return audio
    
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    
    def save_as(self, audio, filename):
        with open(f"{filename}.wav", 'wb') as file:
            file.write(audio.get_wav_data())
    
    def audio_to_text(self, audio):
        try:
            try: #by me
                text = self.recognizer.recognize_google(audio, language="en-us")
            except: # by me
                text = None
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print("Sorry, I couldn't request results from Google Speech Recognition service; {0}".format(e))
    
    def text_to_audio(self, text, lang='en'):
        return gTTS(text, lang)