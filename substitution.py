import pyperclip, sys
import random

LETTERS ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def keyIsValid(key):
    keyList = list(key)
    letterslist = list(LETTERS)
    keyList.sort()
    letterslist.sort()
    print("keyList" + str(len(keyList)))
    
    print("letterslist" + str(len(letterslist)))
    return keyList == letterslist
    
def encryptMg(key, message):
    return TranslateMg(key, message, 'encrypt')

def decryptMg(key, message):
    return TranslateMg(key, message, 'decrypt')

def TranslateMg(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        charsA, charsB = charsB, charsA
    for symbol in message:
        if symbol.upper() in charsA:
            print(symbol.upper())
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            elif symbol.islower():
                translated += charsB[symIndex].lower()
        else:
            translated +=symbol
    return translated

def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return''.join(key)

def main():
    newMg = """If a man is offered a fact which goes against his instinct, he will scrutinize it closely, and unless the evidence is overwhelming,
    he will refuse to believe it."""
    
    key = "LFWOAYUISVKMNXPBDCRJTQEGHZ"
    #key = getRandomKey()
    print(key)
    module = 'encrypt'
    #if keyIsValid(key):
    #    sys.exit("There is error in the key.")
    if module == 'encrypt':
        translated = encryptMg(key, newMg)
    elif module == 'decrypt':
        translated = decryptMg(key, newMg)
        
    print('%sed message:' % (key))
    print("translated " + str(translated))
    pyperclip.copy(str(translated))
    print()
if __name__ == '__main__':
    main()