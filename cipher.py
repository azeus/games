#alpha numeric characters to encrypt/decrypt
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(message,key):
    for character in message:
        num = SYMBOLS.find(character)
        num = num + key
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)
        translated = translated + SYMBOLS[num]
    print(translated)
    return True
        

def decrypt(message,key):
    for character in message:
        if character in SYMBOLS:
            num = SYMBOLS.find(character)
            num = num - key
            if num >= len(SYMBOLS):
                num = num - len(SYMBOLS)
            elif num < 0:
                num = num + len(SYMBOLS)
            translated = translated + SYMBOLS[num]
    print(translated)
    return True


print("Enter you message\n")
message = input('> ')
message=message.upper()
print("Enter your key\n")
key = input('> ')
key = int(key)
print("choose 'e' for encryption and 'd' for decryption")
selection = input("> ")
if selection == 'e':
    encrypt(message,key)
elif selection == 'd':
    decrypt(message,key)
else:
    print('invalid selection\n')

        

