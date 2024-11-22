def get_sum(number):
	
	sum = 0
	for numb in number:
		if numb % 2 == 0:
			sum += numb 
	return sum  

def get_vowel(character):
	vowels = {"A","a","E","e","I","i","O","o","U","u"}
	vowel = 0
	for vol in vowels:
		for char in character: 
			if vol == char:
				vowel +=1
	return vowel

def get_anagram(string_one,string_two):
	for char in string_one:
		if char in string_two:
			return True
 
	return False

def get_prime(number):
	for count in range(2,number):
		if number == 2:
			return True
		if number % count == 0:
			return False
	return True

def get_palindrome(text):
	reversed =""
	for letter in text:
		reversed = letter + reversed
		if reversed in text:
			return True

	return False
		
def get_average(number):
	sum = 0
	average = 0
	for numb in number:
		sum += numb 
		average = sum / len(number)
	return average

def get_reversed(text):
	reversed =""
	for letter in text:
		reversed = letter + reversed
	return reversed 

def get_capitalized(list):
	capitalized=[]
	for word in list:
		capitalized.append(word.capitalize())
	return capitalized
		

def get_duplicate(number): 
	for count in range(len(number)): 
		for counter in range(count + 1, len(number)): 
			if number[count] == number[counter]: 
				return True 
	return False

def remove_spaces(word):
	letters = word.replace(" ","")
	return letters

def get_product_sum(number):
	sum = 0
	for count in range(len(number)):
		sum += (number[count])**2
	return sum

def magic_number(number):
	total = 0
	for count in range(len(number)):
		for numb in number:
			total += numb
		total -= number[count]
	return total

def merge_list(array_one,array_two):
	merge = array_one + array_two
	merge.sort()
	return merge
 
def get_common_elements(list_one,list_two):
	number=[]
	for numbers in list_one:
		if numbers in list_two:
			number.append(numbers)
	return number  
	
def get_sorted_list(list):
	#list.sort(key=len)
	list = sorted(list, key=len)
	return list

def get_factorial(number):
	for count in range(number-1,0,-1):
		number *= count
	return number

def get_digits_sum(number):
	number = str(number)
	sum = 0
	for numb in number:
		numb = int(numb)
		sum += numb
	return sum

def interleave_lists(list1,list2): 
	interleaved = [] 
	len1 = len(list1)
	len2 = len(list2) 
	max_len = max(len1, len2) 
	for count in range(max_len): 
		if count < len1: 
			interleaved.append(list1[count]) 
			if count < len2: 
				interleaved.append(list2[count]) 
	return interleaved

def get_acronym(word):
	acronym = ""
	letters = word.split()
	for letter in letters:
		acronym += letter[0]
	return acronym






	
			
			

 
