def total(number):
	return sum([numb for numb in number if numb % 2 == 0 ])	
number = [2,4,5,6,7,8]
print (total(number))