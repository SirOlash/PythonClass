import math
import random

rand = random.randint(1,1000)
rand2 = random.randint(1,1000)


#def question_generator(questions):
answer = input(int(rand + " + " + rand2))

sum = rand + rand2
if answer == sum: 
	print("Correct!!!")
else: print ("Wrong, the answer is ", sum)

"""print(rand)
print(rand2)
print (sum)"""