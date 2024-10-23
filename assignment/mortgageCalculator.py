principal = float(input("Enter the principal amount: "))

rate = float(input("Enter the annual interest rate: "))
duration = float(input("Enter the duration in years: "))

number_of_years = 12
monthly_rate = (rate/100)/number_of_years
duration_in_months = duration*number_of_years


payment = principal * ((monthly_rate*(1+monthly_rate)**duration_in_months)/((1+monthly_rate)**duration_in_months-1))

print("Your monthly payment is : $%.2f" % payment)

