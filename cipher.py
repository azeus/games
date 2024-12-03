# Alpha numeric characters to encrypt/decrypt
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(message, key):
    translated = ''
    for character in message:
        if character in SYMBOLS:
            num = SYMBOLS.find(character)
            num = (num + key) % len(SYMBOLS)
            translated += SYMBOLS[num]
        else:
            translated += character
    return translated

def decrypt(message, key):
    translated = ''
    for character in message:
        if character in SYMBOLS:
            num = SYMBOLS.find(character)
            num = (num - key) % len(SYMBOLS)
            translated += SYMBOLS[num]
        else:
            translated += character
    return translated

message = input("Enter your message:\n> ").upper()
key = int(input("Enter your key:\n> "))
selection = input("Choose 'e' for encryption or 'd' for decryption:\n> ")

if selection == 'e':
    print("Encrypted message:", encrypt(message, key))
elif selection == 'd':
    print("Decrypted message:", decrypt(message, key))
else:
    print("Invalid selection!")