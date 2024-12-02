#def counter():
	

def even_total(number):
	"""count = 0 
	for numb in number:
		if numb % 2 == 0:
			count +=1
	return count"""
	#return len([numb for numb in number if numb % 2 == 0])
	return sum([1 for numb in number if numb % 2 == 0])



def even_odd(number):
	"""result= []
	for numb in number:
		if numb % 2 == 0:
			result.append(False)
		else: result.append(True)
	return result"""
	return [ True if numb % 2 == 0 else False for numb in number ]
	#return sum([1 for numb in number if numb % 2 == 0])

"""def is_even(x)
	return x % 2 = 0"""


def get_capitalized(words):
	return[word.title() for word in words]

	new_list =[]
	"""for char in words:
		 new_list.append(word.title(char)) 
	return new_list"""

#text.charAt(letter)
#capitalized, title()

def three_multiple(first,second): 
	return [x for x in range (3,31,3)]
	"""multiples = []
	for number in range(first,second):
		if number % 3 == 0:
			multiples.append(number)
	return multiples"""
#def three_multiple()


def odd_square(number): 
	return[numb**2 for numb in number if numb % 2 != 0 ]



"""def is_odd(numbers):
	list(filter(is_odd,numbers))
	return numbers % 2 != 0
	
numbers = [10,3,7,1,9,4,2,8,5,6]

print (is_odd(numb))"""

def numbers_square(number): 
	#return list(filter(lambda number :for number in range(1,number+1)))
	
	return[number**2 for number in range(1,number+1)]

def greater_ten(number): 
	#return list(filter(lambda index: index > 10, number))
	#return list(filter(lambda numb: numb > 10, number))
	return [numb for numb in number if numb > 10]

def palindrome_list(words): 
	return list(map(lambda word: word == word[::-1],words))
	
	"""result = []
	for  word in words:
		reversed = ""
		for letter in word:
			reversed = letter + reversed
		if reversed == word:
			result.append(True)
			
		else: result.append(False)
	return result"""

def string_int(sentence):
	return [int(numb) for numb in sentence if numb.isdigit()]
	
def double(number):
	return [numb*2 for numb in number ]

def longwords(words):
	return [word for word in words if len(word) > 4]

def sum_numb(number):
	return sum([int(numb) for numb in str(number)])

	return sum(list(map(lambda num: int(num),str(number))))
	"""sum = 0
	numb_string = str(number)
	for numb in numb_string:
		sum+= int(numb)		
	return sum"""

"""def remove_vowel(words):
	new_list=[]
	vowels = "A","a","E","e","I","i","O","o","U","u"
	for word in words:
		for vowel in vowels:
			if vowel in word:	
				try = list(word).remove(vowel)
			new_list.append(try)
	return new_list"""

def even_numb(number):
	even = {x:x**2 for x in range(1,number) if x % 2 == 0} 
	return even

def zip_list(my_items,size):
	#return [int(numb) for key,value in zip(my_items,size)}
	our_class = {}
	for key,value in zip(my_items,size):
		our_class[key] = value
	return our_class

def return_value(zip_list):
	for value in zip_list().values:
		return value
	
		








