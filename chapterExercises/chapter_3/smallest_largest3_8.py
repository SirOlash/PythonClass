sum = 0
product = 1
smallest = 9999
largest = 0
for count in range(4):
	number = int(input("Enter number: "))
	sum += number
	average = sum/4
	product *= number 
	if smallest > number:
		smallest = number
	if largest < number:
		largest = number 
print(f"The sum is {sum},\nThe average is {average:.2f},\nThe product is {product},\nThe smallest number is {smallest},\n The largest number is {largest}.") 