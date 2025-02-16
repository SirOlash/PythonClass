import random

def math_quiz():
	answers = []
	sign = ["+","+","+","+","+","*","*","*","-","-"]
	counter = 0
	passed = 0
	failed = 0
	while counter < 10:
		rand1 = random.randrange(1,1000)
		rand2 = random.randrange(1,1000)
		
		response = int(input(f"Calculate {rand1} {sign[counter]} {rand2}: "))
		if counter < 5:
			answer = rand1 + rand2
		elif counter >= 5 and counter <= 7:
			answer = rand1 * rand2
		elif counter >=8 :
			answer = rand1 - rand2
		
		if answer == response:
			passed += 1

		else: 
			failed += 1
			answers.append(f"You missed question {counter 
+1}, The correct answer for {rand1} {sign[counter]} {rand2} is {answer}")

		counter +=1
			
	for result in answers:
		print(result)

	return (f"Your score is {passed} /10 ")

print(math_quiz())
