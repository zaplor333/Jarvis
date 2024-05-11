
from Programs.Hardware.Microphone.microphone import listen
from Programs.Software.Text.textconverter import audio_to_text
from Programs.OS.commands import action

def chat(text):
    return text.split()
    
if __name__=="__main__":
    
    recognizer = sr.Recognizer()
    while True:    
        audio = listen(recognizer)

        text = str(audio_to_text(audio, recognizer))
        action(text.lower())

        print("You: " , text)

    

