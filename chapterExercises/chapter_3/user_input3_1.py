passes = 0
fail = 0 
number = 0


while number != -1:
	number = int(input("Enter 1 for passes and 2 for fails. Enter -1 to stop and calculate: "))
	if number == 2:
		fail +=1
	elif number == 1:
		passes += 1
	else: print ("please enter either 1 or 2")
print(f"There are {passes} passes and {fail} failures")