from jarvis import Jarvis, ChatBot

if __name__ == '__main__':
    jarvis = Jarvis()
    while True:
        audio = jarvis.listen()
        query = jarvis.audio_to_text(audio) # query is None if audio is not recognizable
        if query !=None:
            query = query.lower()
            print("you: ", query)
            response = jarvis.action(query)
            jarvis.speak(response)
    
    

    