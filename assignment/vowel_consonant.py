alphabet = input("Enter a single character from the alphabet: ").lower()

if len(alphabet) == 1 and alphabet.isalpha():
	if alphabet in "aeiou" :
		print("The alphabet entered is a vowel")
	
	else: print("The alphabet entered is a consonant")

else: print("Invalid entry, Please enter a single character of the alphabet")