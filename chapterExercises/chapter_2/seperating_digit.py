integer = int(input("Enter a five digit integer: "))

fifth_number = integer % 10
first_number = integer//10000
fourth_number = (integer // 10) %10
third_number = (integer // 100) %10
second_number = (integer // 1000) %10

print(fifth_number, fourth_number, third_number, second_number, first_number)

