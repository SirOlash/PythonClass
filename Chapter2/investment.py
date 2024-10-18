principal=1000
rate=7
numberOfYears=int(input("Enter the amount of years: "))
amountOnDeposit=principal * (1 + rate)**numberOfYears
print("The amount on deposit after ",numberOfYears,"is", amountOnDeposit)


