mport math
import pyperclip

def decryptMessage(message, key):
    numofcols = int(math.ceil(len(message)/ float(key)))
    numofrows = key
    numofshadow = (numofcols * numofrows) - len(message)
    
    plaintext = [''] *numofcols
    col = 0
    row = 0
    for symbol in message:
        plaintext[col] +=symbol
        col +=1
        if (col == numofcols) or (col == numofcols-1 and row >= numofrows -numofshadow):
            col =0
            row +=1
    return ''.join(plaintext)
    
def main():
    message = "Cenoonommstmme oo snnio. s s c"
    key = 8
    plaintext = decryptMessage(message, key)
    print( plaintext + "|")
    pyperclip.copy(plaintext)

if __name__ == '__main__':
    main() 
