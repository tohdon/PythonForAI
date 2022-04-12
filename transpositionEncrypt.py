import pyperclip

def encryptMessage(key, message):
    ciphertext = [''] * key
    for column in range(key):
        currentIndex = column
        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]
            currentIndex += key
    return ''.join(ciphertext)        
            
def main():
    message = 'Common sense is not a so common'
    key = 8
    ciphertext = encryptMessage(key, message)
    print(ciphertext + '|')
    pyperclip.copy(ciphertext)

if __name__ == '__main__':
    main()