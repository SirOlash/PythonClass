number = int(input("Enter the number to be calculated: "))
terms = int(input("Enter the number of terms: "))

i=0
while i <= terms:
  table = number * i 
  print (number," * ",i, " = ", table)
  i += 1
  
