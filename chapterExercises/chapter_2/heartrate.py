age = int(input("Enter your age: "))


max_heart_rate = 220-age

upper_range = (50/100) * max_heart_rate

lower_range = (85/100) * max_heart_rate

print("the target heart rate is:",max_heart_rate)

print("the range of the user heart rate is:",upper_range,"-",lower_range)