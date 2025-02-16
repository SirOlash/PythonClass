passed = 0
fail = 0

for count in range(1, 16):
	score = int(input("Enter your Score: "))
	if score >= 45:
		passed += 1
	if score < 45:
		fail += 1
print(f"The amount of students that failed are {fail}\nThe amount of students that passed are {passed} ")