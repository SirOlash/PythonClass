def largest_number(number):
	largest = number[0]
	
	for numb in number:
		if numb > largest:
			largest = numb
	return largest

def reversed_number(number):
	reversed = number[::-1] #slice (works like forloop)
	return reversed

def element_occurance(element,number):
	for numb in number:
		if element == numb:
			return True
	return False

def odd_elements(number):
	odd_list = number[1::2]
	return odd_list

def even_elements(number):
	even_list = number[2::2]
	return even_list	

def running_total(numbers):
	runnings = [0] * len(numbers)

	runnings[0] = numbers[0]
	for index in range(1, len(numbers)):
		runnings[index] = runnings[index - 1] + numbers[index]
	return runnings

def string_palindrome(word):
	reversed =""
	for letter in word: 
		reversed = letter + reversed
	if reversed in word:
		return True
	else: return False

def number_sum_for(numbers):
	sum = 0
	for numb in numbers:
		sum += numb
	return sum

def number_sum_while(numbers):
	sum = 0;
	index = 0
	while index < len(numbers):
		sum += numbers[index]
		index +=1
	return sum

def concatenates_list(word,numbers):
	new_list = word + numbers
	return new_list

def alternate_merge(list1, list2):
    merged_list = []
    len1, len2 = len(list1), len(list2)
    max_len = max(len1, len2)

    for i in range(max_len):
        if i < len1:
            merged_list.append(list1[i])
        if i < len2:
            merged_list.append(list2[i])

    return merged_list

def digits_of_number(number):
	digits= []
	for digit in str(number):
		digits.append(int(digit))
	return digits 
	


	
	

	

	