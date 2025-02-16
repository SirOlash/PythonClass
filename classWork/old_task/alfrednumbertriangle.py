number = int(input("enter a number: "))

for count in range(0,number+2):
	print ("")
	for counter in range(1, count):
		print(counter,end=" ")
for height in range(number, 1, -1):
	print("")
	for height2 in range(1,height):
		print (height2, end=" ")

