import math

a = float(input("Input a: "))
b = float(input("Input b: "))
c = float(input("Input c: "))

determinant = b * b - 4 * a * c

root1 = 0
root2 = 0

if determinant > 0: 
	root1 = (-b + math.sqrt(determinant)) / (2 * a)
	root2 = (-b - math.sqrt(determinant)) / (2 * a)
	print(f"The roots are ",root1," and ", root2)

elif determinant == 0: 
	root1 = -b / (2 * a)
	print("The roots are both ",{root1} )

else: print("The roots are not real numbers.")