import codecs
text = input("Enter text:")
key = input("Enter key:")
n = len(text)
cipher = ""
hexlify = codecs.getencoder('hex')
for i in range(n):
	t = text[i]
	k = key[i%len(key)]
	x = ord(k) ^ ord(t)
	cipher += chr(x)
cipher_b = str.encode(cipher)	
print(text, k, hexlify(cipher_b)[0])