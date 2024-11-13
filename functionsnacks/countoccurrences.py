def count_occurrences(character,user_input):
	count = 0
	for char in character:
		if char == user_input:
			count+=1
	return count 

user_input = input("Enter an alphabet: ")
character = input ("Enter a word: ")
print (count_occurrences(character,user_input))
	
	