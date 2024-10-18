integer=int(input("Enter a three digit integer: ")
lastNumber=integer%10
firstNumber=integer//100
firstTwo=integer/10
secondNumber=firstTwo%10
sum=firstNumber+secondNumber+lastNumber
average=sum/3
product=firstNumber*secondNumber*lastNumber
print("The product is ",firstNumber,secondNumber,lastNumber)

