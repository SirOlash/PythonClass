number = int(input("Enter a number between 100-999: "))
lastNumber=number%10
firstNumber=number // 100
firstTwo=number//10
middleNumber=firstTwo%10
print(lastNumber, middleNumber, firstNumber)

odd = 0
even = 0

if firstNumber%2 == 0:
  even +=1
else: odd += 1

if middleNumber%2 == 0:
  even +=1
else: odd +=1

if lastNumber %2 == 0:
  even +=1
else: odd +=1

print("The even number is ", even)
print("The odd number is ", odd)
