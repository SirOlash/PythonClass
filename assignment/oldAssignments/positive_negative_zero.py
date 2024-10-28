positive = 0
negative = 0
zero = 0
i= 0

while(i<5):
	number = int(input("Enter a number: "))

	if(number>0): 
	   positive+=1
	elif(number<0): 
	   negative+=1
	else: 
	   zero+=1
	i+=1

print(f"The number of negatives are: {negative}\nNumber of positives are: {positive}\nNumber of zeros are: {zero}")


