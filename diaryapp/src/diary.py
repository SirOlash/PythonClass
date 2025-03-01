from diaryapp.src.entry import Entry


class Diary:
    def __init__(self, user_name, password):
        self.__user_name = user_name
        self.__password = password
        self.__is_locked = False
        self.__entries = []

        self.__entry_id = 1

    def is_locked(self):
        return self.__is_locked

    def lock_diary(self):
        self.__is_locked = True

    def unlock_diary(self,password):
        if password == self.__password:
            self.__is_locked = False
        else:
            raise Exception("Password doesn't match")

    @property
    def user_name(self):
        return self.__user_name

    def create_entry(self, title, content):
        if not title or title.isspace():
            raise ValueError('Title cannot be empty')
        if not content or content.isspace():
            raise ValueError('Content cannot be empty')
        new_entry = Entry(title, content, self.__entry_id)
        self.__entries.append(new_entry)
        self.__entry_id += 1
        return new_entry

    @property
    def _size(self):
        return len(self.__entries)

    @property
    def entries(self):
        return self.__entries

    def find_entry_by(self,entry_id):
        for entry in self.__entries:
            if entry.get_id == entry_id:
                return entry
        else:
            raise ValueError('Entry not found')

    def delete_entry(self, entry_id):
        entry = self.find_entry_by(entry_id)
        self.__entries.remove(entry)

    def verify_password(self,password:str)-> bool:
        return password == self.__password
        # if password == self.__password:
        #     return True
        # else:
        #     return False

    def update_title(self, entry_id, new_title):
        entry = self.find_entry_by(entry_id)
        entry.title = new_title

    def update_content(self,entry_id,new_content):
        entry = self.find_entry_by(entry_id)
        entry.content = new_content

    def change_password(self,old_password,new_password):
        if old_password == self.__password:
            self.__password = new_password
        else:
            raise Exception("Password doesn't match")





