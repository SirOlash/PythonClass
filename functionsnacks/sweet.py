def count_vowel(word):
	count = 0
	vowels = "AEIOU"
	for vowel in vowels:
		for character in word:
			if vowel == character.upper():
				count +=1 

	return count
user_input = input("Enter a sentence: ")
print (count_vowel(user_input))