def find_number(number_list,number):
	try:
		index = number_list.index(number)
		return index
	except ValueError:
		return Invalid
		
	
	