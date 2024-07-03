from functions import *

from jarvis import Jarvis


if __name__=='__main__':
    jarvis = Jarvis()
    while True:
        audio = jarvis.listen()
        query = str(jarvis.audio_to_text(audio)).lower()
        print(query)
        reply = jarvis.action(query)
        print(reply)
        if reply !=None:
            jarvis.speak(reply)