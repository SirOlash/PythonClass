days_late = int(input("Enter the amount of days late: "))

if days_late <= 5:  
	print ("Your fine is 50Paise")

if days_late > 5 and days_late < 11:
	print ("Your fine is 1 rupee")

if days_late > 10 and days_late < 30:
	print("Your fine is 5 rupees")

if days_late > 30:
	print ("Your membership is cancelled!!!")