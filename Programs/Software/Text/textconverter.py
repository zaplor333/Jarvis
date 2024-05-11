import speech_recognition as sr

def audio_to_text(audio, recognizer=None):
    if recognizer==None:
        recognizer = sr.Recognizer()
    
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Sorry, I couldn't request results from Google Speech Recognition service; {0}".format(e))