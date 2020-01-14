def caesarCipherEncryptor(string, key):
    # Write your code here.

	out = ""
	
	# Get an int representation of the character (using ord)
	for i in string:
		char = ord(i) - ord('a')
		char += key
		
		while char > 25:
			char = char - 26
		
		out += chr(char + ord('a'))
	return out
