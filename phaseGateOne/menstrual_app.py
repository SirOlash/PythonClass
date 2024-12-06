from datetime import datetime,timedelta;

def calender_calculation(cycle_length,period_start_date):
	result = []
	
	start_unsafe = cycle_length - 19
	start_unsafe = period_start_date +timedelta(days=start_unsafe)
	result.append(start_unsafe)

	stop_unsafe = start_unsafe + timedelta(days=11)
	result.append(stop_unsafe)

	stop_safe = start_unsafe - timedelta(days=1)
	result.append(stop_safe)

	start_ovulation = start_unsafe + timedelta(days=5)
	result.append(start_ovulation)

	stop_ovulation = start_ovulation + timedelta(days=1)
	result.append(start_ovulation)

	second_start_safe = stop_unsafe + timedelta(days=1)
	result.append(second_start_safe)

	stop_second_safe = period_start_date + timedelta(days=cycle_length)
	result.append(stop_second_safe)


	return result






def menstrual_app():
	user_name = input("Hello, Enter your name: ") 
	user_age = int(input("Enter your age: "))
	
	if user_age >= 11 and user_age <= 50:
		print("***This is just a prediction, it is not entirely accurate. This calendar method and would mostly work for periods that are regular and menstrual cycles that falls within the range of 26 - 30days.***")

		period_start_date = None
		date_format = "%Y-%m-%d" 

		while period_start_date is None:
			try:
				date_input = input("Enter the date you started your period (yyyy-MM-dd): ")
				period_start_date = datetime.strptime(date_input, date_format)
			except ValueError:print("Invalid date format. Please use the format yyyy-MM-dd.")

		cycle_length = int(input("How many days was your last menstral cycle: "))
	
		result = calender_calculation(cycle_length,period_start_date)

		print("Hello " + user_name)


	#end_date = period_start_date + timedelta(days=results[2])


		print(f"Your first safe period should start from {period_start_date.strftime('%Y-%m-%d')} and end at {result[2].strftime('%Y-%m-%d')}.") 
		print(f"Your unsafe period should start from {result[0].strftime('%Y-%m-%d')} and end at {result[1].strftime('%Y-%m-%d')}.") 
		print(f"Your ovulation period should start from {result[3].strftime('%Y-%m-%d')} and end at {result[4].strftime('%Y-%m-%d')}.") 
		print(f"Your second safe period should start from {result[5].strftime('%Y-%m-%d')} and end at {result[6].strftime('%Y-%m-%d')}.")
	
	else: print("You shouldn't be Mensurating, See a doctor!!!")
	
menstrual_app()
	
		
