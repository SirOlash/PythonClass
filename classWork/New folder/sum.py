"""def is_even(number):
	sum = 0
	for numb in number:
		if numb % 2 == 0:
			sum += numb	 
	return sum """


"""def is_prime(number):
	prim = 0
	prime = []
	for index in range(3,number):
		for counter in range(2,index):
			if index % counter == 0:
				break 
		
	prime.append(index)

	return prime"""

def total(number):
	return sum([numb for numb in number if numb % 2 == 0 ])	
	number = [2,4,5,6,7,8]	

	"""tot = 0
	for numb in number:
		tot+= numb
	return tot ""
print (total(number))

def cube(number):
	return[numb**3 for numb in number]
	"""cub = []
	for numb in number:
		cub.append(numb**3)
	return cub"""




def list():
	return(cube([x for x in range (1,6)]))

	
	"""numb = []
	for index in range(1,number+1): 
		numb.append(index)
	return numb
number = 5"""
print (list())