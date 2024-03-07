import sys
import pyttsx3


'''3 modes of operation
1. read the line entered
2. read a PDF/txt
3. read a website
'''
tts = pyttsx3.init()
print('Enter text to speak\n')
text = input('> ')
tts.say(text)
tts.runAndWait()