

x = int(input("Enter the minimum range: "))
y = int(input("Enter the max range: "))
p = int(input("Enter the step value: "))

count = 0
total = 0
for value in range(x, y, p):
    total += 1
    if value % 3 == 0:
     count += 1
   # print(value)
   
print (f"Total number of values: {total}")
print(f"Total number of values divisible by {p}: {count}")
