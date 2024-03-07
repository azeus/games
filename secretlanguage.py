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

print('enter your message\n')
message = input('>')
lang = ''
for word in message.split():
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()

    if len(word)> 0 and not word[0] in VOWELS:
        consonant = word[0]
        word = word[1:]
    if consonant != '':
        word += consonant + 'bub'
    else:
        word += 'bub'
    
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    lang += word 
print(lang)


    



