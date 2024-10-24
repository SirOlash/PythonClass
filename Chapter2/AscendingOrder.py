integer=float(input("Enter a three digit integer: "))

lastNumber=integer%10
firstNumber=integer//100
firstTwo=integer//10
secondNumber=firstTwo%10

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

if firstNumber != largest and firstNumber != smallest:
	inBetween = firstNumber
if secondNumber != largest and secondNumber != smallest:
	inBetween = secondNumber
if lastNumber != largest and lastNumber != smallest:
	inBetween = lastNumber

print(largest)
print(inBetween)
print(smallest)