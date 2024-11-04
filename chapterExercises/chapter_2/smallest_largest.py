integer = int(input("Enter a three digit integer: "))

lastNumber = integer%10
firstNumber = integer//100
firstTwo = integer//10
secondNumber = firstTwo%10

sum = firstNumber+secondNumber+lastNumber
average = sum/3
product = firstNumber*secondNumber*lastNumber


if firstNumber > secondNumber and firstNumber > lastNumber:
	largest=firstNumber

if secondNumber > firstNumber and secondNumber > lastNumber:
	largest=secondNumber
if lastNumber > firstNumber and lastNumber > secondNumber:
	largest=lastNumber


if firstNumber < secondNumber and firstNumber < lastNumber:
	smallest=firstNumber

if secondNumber < firstNumber and secondNumber < lastNumber:
	smallest=secondNumber
if lastNumber < firstNumber and lastNumber < secondNumber:
	smallest=lastNumber

print("The sum is ",sum)
print("The average is ",average)
print("The product is ",product) 
print("The smallest is ",smallest)
print("The largest is ",largest)

