import pyttsx3

def text_to_speech():
    try:
        tts = pyttsx3.init()
        print('Enter text to speak:')
        text = input('> ')
        tts.say(text)
        tts.runAndWait()
    except Exception as e:
        print("An error occurred with Text-to-Speech:", e)

text_to_speech()