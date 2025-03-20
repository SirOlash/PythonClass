import re
from services.user_registration import Registration


class CourseMenu:
    def main(self):
        self.course_main()

    def course_main(self):
        while True:
            print("""
             Welcome to Course Management System!
                1. Login
                2. Register 
                3. Exit
                """)

            choice = self.valid_int("Enter your choice: ")
            match choice:
                case "1":
                    while True:
                        print(""""
                         1. Login as a Student
                         2. Login as a Facilitator
                         3. Go back to main menu
                        """)
                        login_choice = self.valid_int("Enter your choice: ")
                        match login_choice:
                            case "1":
                                self.student_login()
                                break
                            case "2":
                                self.facilitator_login()
                                break
                            case "3":
                                self.course_main()
                                break
                            case _:
                                print("Invalid input")
                case "2":
                        self.user_register()
                        break
                case "3":
                        print("Goodbye, Thank you for using our app!")
                        exit()
                case _: print("invalid input")

    def student_menu(self,student):
        while True:
            print(f"""
             Welcome to Your Student Menu {student.last_name}!
                1. View All Courses 
                2. Register For A Course 
                3. View Your Registered Courses
                4. Go to Main Menu
                """)

            choice = self.valid_int("Enter your choice: ")
            match choice:
                case "1":
                        self.view_all_course(student)
                        break
                case "2":
                        self.register_for_a_course(student)
                        break
                case "3":
                        self.view_registered_course(student)
                        break
                case "4":
                        self.course_main()
                        break
                case _: print("invalid input")

    def facilitator_menu(self,facilitator):
        while True:
            print(f"""
             Welcome to Your Menu Mr/Mrs {facilitator.last_name}!
                1. Create A Course
                2. View Registered Students
                3. Assign Grade
                4. Go back to Main Menu
                """)

            choice = self.valid_int("Enter your choice: ")
            match choice:
                case "1":
                        self.create_courses(facilitator)
                        break
                case "2":
                        self.view_reg_student(facilitator)
                        break
                case "3":
                        self.assign_grades(facilitator)
                        break
                case "4":
                        self.course_main()
                        break
                case _: print("invalid input")

    def student_login(self):
        try:
            email = self.valid_email("Enter your user email: ")
            password = self.valid_password("Enter your user password: ")
            current_student = Registration.login_student(email,password)
            print("You have logged in as a student")
            self.student_menu(current_student)

        except Exception as e:
            print(f"{e}")
            self.course_main()

    def facilitator_login(self):
        try:
            email = self.valid_email("Enter your user email: ")
            password = self.valid_password("Enter your user password: ")
            current_facilitator = Registration.login_facilitator(email, password)
            print(f"You are logged in as a facilitator")
            self.facilitator_menu(current_facilitator)

        except Exception as e:
            print(f"{e}")
            self.course_main()

    def create_courses(self,current_facilitator):
        course_name = self.valid_course("Enter course name: ")
        try:
            current_facilitator.create_course(course_name)
            print(f"you have created {course_name}")


        except Exception as e:
            print(f"{e}")
        finally:
            self.facilitator_menu(current_facilitator)


    def view_reg_student(self,current_facilitator):
        try:
            reg_students = current_facilitator.view_registered_students()
            print(reg_students)
        except Exception as e:
            print(f"{e}")
        finally:self.facilitator_menu(current_facilitator)

    def assign_grades(self,current_facilitator):
        course_name = self.valid_course("Enter course name: ")
        student_email = self.valid_email("Enter the student email: ")
        student_mark = self.valid_score("Enter the student score: ")
        try:
            current_facilitator.assign_grade(course_name,student_email,student_mark)
            print(f"you have assigned {student_mark} to {student_email} for {course_name}")

        except Exception as e:
            print(f"{e}")
        finally:
            self.facilitator_menu(current_facilitator)


    def user_register(self):
        first_name = self.valid_name("Enter your first name: ")
        last_name = self.valid_name("Enter your last name: ")
        user_email = self.valid_email("Enter your user email: ")
        user_password = self.valid_password("Enter your password: ")
        user_choice =self.valid_reply("Are you a student or facilitator? (S/F): ")

        if user_choice.lower() == "s":
            Registration.register_student(first_name, last_name, user_email, user_password)
            print("You have successfully registered as a student.")
            self.course_main()
        else:
            Registration.register_facilitator(first_name, last_name, user_email, user_password)
            print("You have successfully registered as a facilitator.")
            self.course_main()



    def view_registered_course(self,current_student):
        registered_courses = current_student.view_registered_courses()
        print(registered_courses)
        self.student_menu(current_student)


    def register_for_a_course(self,current_student):
        try:
            courses = current_student.view_available_courses()
            print(courses)
            course_name = self.valid_course("Enter course name: ")
            current_student.register_for_course(course_name)
            print(f"You have successfully registered for {course_name}")
        except Exception as e:
            print(f"{e}")

        finally:self.student_menu(current_student)


    def view_all_course(self,current_student):
        courses = current_student.view_available_courses()
        print(courses)
        self.student_menu(current_student)

    @staticmethod
    def valid_score(prompt):
        while True:
            user_input = int(input(prompt))
            if 0 <= user_input <= 100:
                return user_input
            else:
                print("Enter a valid score between 0 and 100")

    @staticmethod
    def valid_course(prompt):
        while True:
            user_input = input(prompt)
            if re.fullmatch(r'[A-Za-z0-9]+', user_input):
                return user_input
            else:
                print("Password must contain at least 4 characters")

    @staticmethod
    def valid_password(prompt):
        while True:
            user_input = input(prompt)
            if re.fullmatch(r'[A-Za-z@_$#\d]{4,}', user_input):
                return user_input
            else:
                print("Password must contain at least 4 characters")

    @staticmethod
    def valid_email(prompt):
        while True:
            user_input = input(prompt).strip()
            if re.fullmatch(r'^[A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]{2,}$', user_input):
                return user_input

            else:
                print("Enter a valid email")

    @staticmethod
    def valid_name(prompt):
        while True:
            user_input = input(prompt).strip()
            if re.fullmatch(r'^[A-Za-z]+', user_input):
                return user_input

            else:
                print("Enter a valid input")

    @staticmethod
    def valid_reply(prompt):
        while True:
            user_input = input(prompt).strip()
            if re.fullmatch(r"^([SsFf])$", user_input):
                return user_input

            else:
                print("Enter either S or F")

    @staticmethod
    def valid_int(prompt):
        while True:
            user_input = input(prompt).strip()
            if re.fullmatch(r"^[0-9]$", user_input):
                return user_input
            else:
                print("Enter a valid input")



if __name__ == "__main__":
    course_menu = CourseMenu()
    course_menu.main()



