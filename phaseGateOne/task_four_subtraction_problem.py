"""generate two random numbers 
	create a loop that runs 10 times
	check if random_number_one > random_number_two
	if it is, prompt user to calculate 10 questions 
	print the passed / failed  """ 

import random
import time 

def subtraction_problem():
	counter = 0
	passed = 0
	failed = 0
	while counter < 10:
		random_number_one = random.randrange(1,100)
		random_number_two = random.randrange(1,100)
	
		if random_number_one > random_number_two:
			response = int(input(f"Calculate {random_number_one} - {random_number_two}: "))

			answer = random_number_one - random_number_two
		
			if answer == response:
				passed += 1

			else:failed += 1


		else: counter -=1

		counter +=1
			

	return (f"Your score is {passed} / {failed}")

print(subtraction_problem())