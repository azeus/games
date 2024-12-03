'''
two versions of this game:
basic :
    choose between 'lup', 'strum', 'sas', 'bub'
advanced:
    combination of above at random
words starting with a vowel only add the
above phrase in the end and the rest will add
the phrase in the ending of the word
and remove the the orginal first letter and add it before 
the add-on phrase
'''

VOWELS = 'aeiou'

print('Enter your message:')
message = input('> ')
lang = ''

for word in message.split():
    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower()
    consonant = ''
    if len(word) > 0 and word[0] not in VOWELS:
        consonant = word[0]
        word = word[1:]

    if consonant:
        word += consonant + 'bub'
    else:
        word += 'bub'

    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()

    lang += word + ' '

print("Translated message:", lang.strip())

    



