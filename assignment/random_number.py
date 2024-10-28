import random

random_number = random.randint(1,9)
guess = -1
while guess != random_number:
	
	guess = int(input("Guess the number: "))
	if guess < random_number:
		print("Too low, try again")

	if guess > random_number: 
		print("Too high, try again")

	if guess == random_number:
		print("Congratulations!!! you are correct")
	
