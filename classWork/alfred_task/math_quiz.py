import random

def math_quiz():
	right_answer = []
	sign = ["+","-","*"]
	passed = 0
	failed = 0
	count = 0
	while count < 5:
		
		rand1 = random.randrange(1,20)
		rand2 = random.randrange(1,20)
		counter = random.randrange(0,3)
		 
		while True:
			try:
				response = int(input(f"What is {rand1} {sign[counter]} {rand2}: "))
			
			
				print (f"Your answer is: {response}")
		
				if counter == 0:
					answer = rand1 + rand2
				elif counter == 1:
					answer = rand1 - rand2
				elif counter == 2:
					answer = rand1 * rand2
		
				if answer == response:
			
					passed += 1

				else: 
					failed += 1
					right_answer.append(f"You missed question {count 
+1}, The correct answer for {rand1} {sign[counter]} {rand2} is {answer}")

				if response == answer:
					print("Correct")
				else: print("Wrong")  

				count +=1
				break
			except ValueError: 
				print("invalid input")
				
			
	for result in right_answer:
		print(result)
	if passed < 3:
		print("OLODO RABATA!!!")
	else: print("You are Good!!!")
	return (f"Your score is {passed} / 5")
	
	
print(math_quiz())