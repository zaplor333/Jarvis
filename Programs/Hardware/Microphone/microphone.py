import speech_recognition as sr

def listen(recognizer=None):
    if recognizer==None:
        recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)
    return audio