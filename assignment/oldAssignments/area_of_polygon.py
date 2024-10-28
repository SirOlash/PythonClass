import math
number_of_sides = int(input("Enter number of sides: "))
length_of_side = int(input("Enter length of sides: "))
pie = 3.14

area = (number_of_sides * (length_of_side**2))/(4 * math.tan(3.14/number_of_sides))

print(f"The area is {area:.4f}")