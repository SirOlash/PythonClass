from diary import Diary

class Diaries:

    diary_list = []

    def create_diary(self, user_name, password):
        if not user_name or user_name.isspace():
            raise ValueError("Username cannot be empty")
        if not password or password.isspace():
            raise ValueError("Password cannot be empty")
        self.diary_list.append(Diary(user_name, password))


    def find_diary_by(self, user_name):
        for diary in self.diary_list:
            if diary.user_name == user_name:
                return diary
        else:
            raise ValueError("Diary not found")

    def delete_diary(self, user_name:str,password:str):
        diary = self.find_diary_by(user_name)
        if diary.verify_password(password):
            self.diary_list.remove(diary)
        else:
            raise ValueError("Password doesn't match")

    def _size(self):
        return len(self.diary_list)

