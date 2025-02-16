def evenodd():
	numberlist=[1,2,3,6,8,10,1]
	odd = 0
	even = 0
	for num in numberlist:
		if num % 2 == 0:
			even += 1
		else:
			odd += 1
	return [odd, even]
print(evenodd())


def oddeven():
	numberlist=[5,3,7,9,2,8]
	odd = 0
	even = 0
	for num in numberlist:
		if num % 2 == 0:
			even += 1
		else:
			odd += 1

	return [odd, even]
print(oddeven())
	