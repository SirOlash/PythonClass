from diaries import Diaries
import time
class DiaryMenu:
    def __init__(self):
        self.diaries = Diaries()
    def main(self):
        self.go_to_main_menu()

    def go_to_main_menu(self):
        while True:
            print("""
             Welcome!!! What would you like to do?
                1. Create a new diary
                2. Enter Your Diary
                3. Delete Your Diary
                4. Exit
                """)

            choice = input("Enter your choice: ")
            match choice:
                case "1":
                        self.create_diary()
                        break
                case "2":
                        self.enter_diary()
                        break
                case "3":
                        self.delete_diary()
                        break
                case "4":
                        print("Goodbye, Thank you for using our diary!")
                        exit()
                case _: print("invalid input")


    def diary_menu(self,user_name):
        while True:
            print(f"""Welcome to your Diary {user_name}
            1. Create a new Entry
            2. View Entry
            3. Delete Entry
            4. Lock Diary
            5. Unlock Diary
            6. Change Title
            7. Change Content
            8. Change Password
            9. Go To Main Menu""")

            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    self.create_entry(user_name)
                    break
                case "2":
                    self.view_entry(user_name)
                    break
                case "3":
                    self.delete_entry(user_name)
                    break
                case "4":
                    self.lock_diary(user_name)
                    break
                case "5":
                    self.unlock_diary(user_name)
                    break
                case "6":
                    self.change_title(user_name)
                    break
                case "7":
                    self.change_content(user_name)
                    break
                case "8":
                    self.change_password(user_name)
                    break
                case "9": self.go_to_main_menu()

                case _: print("invalid input")

    def change_password(self, user_name):
        diary = self.diaries.find_diary_by(user_name)
        if not diary.is_locked():
            old_password = self.valid_string("Enter your old password: ")
            if diary.verify_password(old_password):
                new_password = self.valid_string("Enter your new password: ")
                diary.change_password(old_password,new_password)
                self.loading_screen("Processing")
                print("Your password has been changed successfully")
                self.diary_menu(user_name)
            else:
                print("Invalid password")
                self.diary_menu(user_name)
        else:
            print("Your password is locked, unlock diary to continue")
            self.diary_menu(user_name)

    def change_content(self,user_name):
        diary = self.diaries.find_diary_by(user_name)
        if not diary.is_locked():
            try:
                user_id = int(input("Enter your ID: "))
                diary.find_entry_by(user_id)
                new_content = self.valid_string("Enter new content: ")
                diary.update_content(user_id, new_content)
                print("Your new content has been updated.")
            except ValueError as e:
                print(e)
            finally: self.diary_menu(user_name)

        else:
            print("Diary is locked, unlock to continue")
            self.diary_menu(user_name)

    def change_title(self, user_name):
        diary = self.diaries.find_diary_by(user_name)
        if not diary.is_locked():
            try:
                user_id = int(input("Enter your ID: "))
                diary.find_entry_by(user_id)
                new_title = self.valid_string("Enter new title: ")
                diary.update_title(user_id,new_title)
                print(f"Your entry has been updated to: '{new_title}' successfully!")
            except ValueError as e:
                print(e)
            finally: self.diary_menu(user_name)
        else:
            print("Diary is locked, unlock to continue")
            self.diary_menu(user_name)

    def lock_diary(self, user_name):
        diary = self.diaries.find_diary_by(user_name)
        if not diary.is_locked():
            diary.lock_diary()
            print("Diary is locked successfully!")
            self.diary_menu(user_name)
        else:
            print("Diary is already locked!")
            self.diary_menu(user_name)


    def unlock_diary(self, user_name):
        diary = self.diaries.find_diary_by(user_name)
        if  diary.is_locked():
            try:
                password = self.valid_string("Enter your password: ")
                diary.unlock_diary(password)
                print("Your diary has been unlocked successfully!")

            except Exception as error:
                print(error)
            finally: self.diary_menu(user_name)

        else:
            print("Your diary is already unlocked!")
            self.diary_menu(user_name)

    def delete_entry(self, user_name):
        diary = self.diaries.find_diary_by(user_name)
        if not diary.is_locked():
            try:
                user_id = int(input("Enter your ID: "))
                diary.delete_entry(user_id)
                self.loading_screen("Deleting entry")
                print("Your entry has been deleted")
            except ValueError as error:
                print(error)
            finally:self.diary_menu(user_name)

    def view_entry(self, user_name):
        diary = self.diaries.find_diary_by(user_name)
        if not diary.is_locked():
            try:
                user_id = int(input("Enter your ID: "))
                entry = diary.find_entry_by(user_id)
                print(entry)

            except ValueError as error:
                print(error)
            finally: self.diary_menu(user_name)

        else:
            print("Diary is locked, please unlock to continue")
            self.diary_menu(user_name)


    def create_entry(self,user_name):
        diary = self.diaries.find_diary_by(user_name)
        if not diary.is_locked():
            title = self.valid_string("Enter title: ")
            content = self.valid_string("Enter content: ")
            entry = diary.create_entry(title,content)
            self.loading_screen("Creating Entry")
            print(f"Your entry with ID: {entry.get_id} has been saved successfully!")
            self.diary_menu(user_name)
        else:
            print("Diary is locked! please unlock to continue.")
            self.diary_menu(user_name)

    def delete_diary(self):
        try:
            user_name = self.valid_name("Enter your name: ")
            self.diaries.find_diary_by(user_name)
            password = self.valid_string("Enter your password: ")
            self.diaries.delete_diary(user_name, password)
            self.loading_screen("Deleting Diary")
            print("You have successfully deleted your diary.")
        except ValueError as e:
            print(e)
        finally:
            self.go_to_main_menu()


    def enter_diary(self):
        try:
            user_name = self.valid_name("Enter your name: ")
            self.diaries.find_diary_by(user_name)
            self.diary_menu(user_name)
        except ValueError as e:
            print(e)
            self.go_to_main_menu()


    def create_diary(self):
        user_name = self.valid_string("Enter your name: ")
        password = self.valid_string("Enter your password: ")
        self.diaries.create_diary(user_name, password)
        self.loading_screen("Creating Diary")
        print("You have successfully created a diary!")
        self.diary_menu(user_name)


    @staticmethod
    def valid_string(prompt: str):
        while True:
            user_input = input(prompt).strip()
            if user_input:
                return user_input
            else:
                print("Please enter a valid string")


    @staticmethod
    def valid_name(prompt: str):
        while True:
            user_input = input(prompt).strip()
            if user_input.isalpha():
                return user_input
            else:
                print("Please enter a valid string")

    def loading_screen(message):
        print(message, end='')
        for index in range(1, 6):
            print(">", end='')
            time.sleep(1)
        print()


if __name__ == "__main__":
    diary_menu = DiaryMenu()
    diary_menu.main()










