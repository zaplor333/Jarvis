import os

def action(string):
    if string == "open youtube":
        import webbrowser
        webbrowser.open('https://www.youtube.com')
    
    if string == "open notepad":
        os.system("notepad.exe")