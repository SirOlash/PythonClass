weight = float(input("Enter your weight in Kilograms: "))
height = float(input("Enter your height in meters: "))

heightSquared = height * height

bmi = weight/heightSquared

print(f"Your BMI is: {bmi:.3f}");