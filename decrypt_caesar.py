"""
Code for decrypting a message that is encrypted using Caesar's cipher. The key for the ciphering scheme is based on the word "UNICORN" 
where the sum of letters in the sublist "CORN" is subtracted by sum of letters in the sublist "UNI" with C = 9 and I = 27
i.e. key = sum(CORN)-sum(UNI)

Input: encrypted_message
Output: decrypted message

function call: decrypt(encrypted_message)

"""
#cipher_key is the hash function that accepts a base as the input parameter and returns its numeric key (18 for UNICORN)

def cipher_key(base):

	if base != "UNICORN":
		return False
		
	else:
		left = base[:3]
		right = base[3:]
		sum_left  = 0
		sum_right = 0
		for char in left:
			num = ord(char)-64
		
			sum_left+= (num)*3
		
		for char in right:
			num = ord(char)-64
			sum_right+= (num)*3
		
		key = sum_right-sum_left
		
		return key

#show_key checks if the logic of cipher_key is correct

def show_key(base):
	print ("Cipher function works!" if cipher_key(base)==18 else "Oops, try again!")



print(show_key("UNICORN"))

#decrypt deciphers the encrypted message where each character in the encrypted message is decrypted with the formula:
#deciphered character = (encrypted character - key)*mod 26 and key is generated using cipher_key

def decrypt(text):
	lower_text = text.lower()  #change all chars in text to lower case
	word_list = lower_text.split(' ') #split word into list of words using whitespace as the delimiter
	decrypt_list = list()  #initialize an empty list literal to hold all decrypted words
	original = '' #initialize an empty string to store the decrypted message
	
	for word in word_list:
		decrypt_word = ''  #an empty string for storing the decrypted characters of a word in the list of words
		for char in word:
			num = ord(char)-97 #change char to numeric equiv by subtracting 97 from its ascii equivalent
			decrypt_word +=chr(((num-cipher_key("UNICORN"))%26)+97) #apply the decryption formula and convert result to character equivalent
		
		decrypt_list.append(decrypt_word) #add decrypted word to decrypted list
		
	for word in decrypt_list:
		original+=word+' '
		
		original = original[0].upper() + original[1:]
	return original[:-1]  #delete the last spacing
	
	
#Test decryption
encrypt_text = "Gnwj gfw eaddagf ewjuzsflk sfv ugmflafy"
print("The decrypted message that was sent between the interns is: {}".format(decrypt(encrypt_text)))  #Decrypted message is: Over one million merchants and counting
