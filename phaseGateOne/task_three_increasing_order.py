"""prompt user to enter first,second and third number respectively
save as first_number,second_number,third_number
use if statements to check for the greater number in first_number,second_number,third_number
display the gretest followed by the second greatest then the third greatest"""

"""first = 0
second = 0
third = 0

first_number = int(input("Enter first number: "))

second_number = int(input("Enter second number: "))

third_number = int(input("Enter third number: "))

if first_number > second_number and first_number > third_number :
	first = first_number 

if third_number > second_number and third_number > first_number :
	first = third_number 

if second_number > first_number and second_number > third_number :
	first = second_number

if first_number > second_number and first_number < third_number :
	second = first_number 

if first_number < second_number and first_number > third_number :
	second = first_number 

if third_number > second_number and third_number < first_number :
	second = third_number 

if third_number < second_number and third_number > first_number :
	second = third_number 

if second_number > first_number and second_number < third_number :
	second = second_number

if second_number < first_number and second_number > third_number :
	second = second_number

if first_number < second_number and first_number < third_number :
	third = first_number 

if third_number < second_number and third_number < first_number :
	third = third_number 

if second_number < first_number and second_number < third_number :
	third = second_number

print(f"{first}{second}{third}")"""


list=[]

first_number = int(input("Enter first number: "))
list.append(first_number)

second_number = int(input("Enter second number: "))
list.append(second_number)

third_number = int(input("Enter third number: "))
list.append(third_number)
list.sort(reverse = True)


print (list)


