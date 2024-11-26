def switchlist(number_list,number):
	moved_number = number_list[:number:] 
	remaining = number_list[number::]
	new_list = remaining + moved_number

	return new_list

def odd_even(number):
	result = []
	for numb in number:
		if numb % 2 == 0:
			result.append(True)
		if numb % 2 != 0:
			result.append(False)
	return result

def seperate(number):
	result = []
	if len(number) % 2 == 0:
		toty = len(number) // 2
		first_set = number[:toty:]
		second_set = number[toty::]
		result.append(first_set) 
		result.append(second_set) 
		return result

	if len(number) % 2 != 0: 
		tot = len(number) // 2 
		first_set = number[:tot+1:]
		second_set = number[tot+1::]
		result.append(first_set) 
		result.append(second_set) 
		return result
		
		
		
	
	
	
