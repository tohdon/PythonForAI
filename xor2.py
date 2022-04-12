text = input("Enter text:")
key = input("Enter key:")
n = len(text)
for i in range(n):
	t = text[i]
	k = key[i%len(key)]
	x = ord(k) ^ ord(t)
	print(t, k, t, x, chr(x))