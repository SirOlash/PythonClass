answer = "yes"

while answer.lower == "yes":
	number = int(input("Enter a number: "))
	
	largest = max(number)
	smallest = min(number)

	answer= input("Do you want to add more numbers? yes/no: ")
	
print(f"The Largest number is:{largest} The Smallest number is: {smallest}") 	


numbers = []

answer = "yes"
while answer.lower() == "yes":
    number = int(input("Enter a number: "))
    numbers.append(number)
    answer = input("Do you want to add more numbers? yes/no: ")

largest = max(numbers)
smallest = min(numbers)

print(f"The Largest number is: {largest}")
print(f"The Smallest number is: {smallest}")

	