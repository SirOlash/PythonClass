""" put the days of the week inside a list 
prompt user to enter today's day
save as "today_day"
prompt user to enter the number of days elapsed since today
save as "total_days"

calculate today_day + days_elapsed 
save result as "total_days"

for days above 6 use a module to get the remainder after dividing by 7, use the remainder as an index to get the particular weekday on the list

display the day and the future day"""



week_day = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

today_day = int(input("Enter today's day: "))
if 
days_elapsed = int(input("Enter the number of days elapsed since today: "))

total_days = today_day + days_elapsed 

if total_days > 6:
	total_days %= 7  

print(f"Today is {week_day[today_day]} and the future day is {week_day[total_days]} ")

