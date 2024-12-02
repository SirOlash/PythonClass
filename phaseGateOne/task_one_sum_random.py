import random

random_number_one = random.randint(1,100)
random_number_two = random.randint(1,100)
sum = random_number_one + random_number_two 

user_input = float(input(f"Enter the sum of {random_number_one} and  {random_number_two}: "))

if user_input == sum:
	print("True")
else: print("False")