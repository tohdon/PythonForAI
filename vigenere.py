import pyperclip

LETTERS ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encryptMg(key, message):
    return TranslateMg(key, message, 'encrypt')

def decryptMg(key, message):
    return TranslateMg(key, message, 'decrypt')

def TranslateMg(key, message, mode):
    translated = []
    keyIndex = 0
    key = key.upper()
    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])
            
            num %= len(LETTERS)
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)
    return ''.join(translated)


def main():
    newMg = """Alan Turing is mathematician, logican, crytanalyst, and computer scientist"""
    key = "ASIMOV"
    module = 'encrypt'
    
    if module == 'encrypt':
        translated = encryptMg(key, newMg)
    elif module == 'decrypt':
        translated = decryptMg(key, newMg)
        
    print('%sed message:' % (module.title()))
    print(translated)
    pyperclip.copy(translated)
    print()
if __name__ == '__main__':
    main()