from dotenv import load_dotenv;load_dotenv()
import os

name = os.getenv('name')

pairs = [
    ['hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']],
    ['how are you', ['I am good, thank you!', 'Doing well, thanks!', 'Not too bad.']],
    ['what is your name', [f'my name is {name}.']],
    ['bye|goodbye', ['Goodbye!', 'Bye!', 'Take care!']],
]