gallons_used = 0
while gallons_used != -1:
	gallons_used = float(input("Enter the amount of gallons used. -1 to end: "))
	if gallons_used != -1:
		miles_driven = int(input("Enter the amount of miles driven: "))
		miles_gallon = miles_driven / gallons_used
		print ("The miles/gallon for this tank was ",miles_gallon)
	 
