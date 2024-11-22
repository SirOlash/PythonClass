def get_student_grade():
	python = [50 , 60, 70, 30, 80, 65, 45, 20, 90, 20]
	java = [30, 50, 45, 60, 75, 80, 90, 100, 55, 60]
	data_science = [100, 80, 45, 50, 60, 75, 85, 20, 10, 65]
	design_thinking = [95, 90, 80, 50, 60, 66, 55, 75, 85, 100]
	student_name = ["Gloria", "Divine", "Bibi", "Emma", "Chris", "Samuel", "Moses", "Leke", "Tosin"]

	best_student_py = python[0]
	best_student_java = java[0]
	best_student_ds = data_science[0]
	best_student_design = design_thinking[0]

	least_student_py = python[0]
	least_student_java = java[0]
	least_student_ds = data_science[0]
	least_student_design = design_thinking[0]

	for count in python:
		if count > best_student_py:
			best_student_py = count
			#student_name[count] = best_student_py
		elif count < least_student_py:
			least_student_py = count
		#print(student_name[count])

	for count in java:
		if count > best_student_java:
			best_student_java = count
		elif count < least_student_java:
			least_student_java = count

	for count in data_science:
		if count > best_student_ds:
			best_student_ds = count
		elif count < least_student_ds:
			least_student_ds = count

	for count in design_thinking:
		if count > best_student_design:
			best_student_design = count
		elif count < least_student_design:
			least_student_design = count


	#for counter in range(len(student_name)):
		#print(f"{student_name[counter]}:\t{python[counter]}\t{java[counter]}\t{data_science[counter]}\t{design_thinking[counter]}\n")


	print(f"The best grade in python is {best_student_py}, The best student is:  {student_name[python.index(best_student_py)]}\n")
	print(f"The least grade in python is {least_student_py}, The least student is:  {student_name[python.index(least_student_py)]}\n")
	
	print(f"The best grade in java is {best_student_java}, The best student is: {student_name[java.index(best_student_java)]}\n")
	print(f"The least grade in java is {least_student_java}, The least student is: {student_name[java.index(least_student_java)]}\n")

	print(f"The least grade in Data science is {least_student_ds}, The best student is: {student_name[data_science.index(best_student_ds)]}\n")
	print(f"The best grade in Data science is {best_student_ds}, The least student is:  {student_name[data_science.index(least_student_ds)]}\n")

	print(f"The best grade in Design thinking is {best_student_design}, The best student is: {student_name[design_thinking.index(best_student_design)]}\n")
	print(f"The least grade in Design thinking is {least_student_design}, The least student is: {student_name[design_thinking.index(least_student_design)]}\n")

		
get_student_grade()