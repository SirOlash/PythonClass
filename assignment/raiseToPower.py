first_number=int(input("Enter first Number: "))
second_number=int(input("Enter second Number: "))

i=0
raise_to_power=1

while(i<second_number):
   raise_to_power*= first_number
   i+=1
	
print (first_number, " raised to the power of  ", second_number, " is ",raise_to_power) 