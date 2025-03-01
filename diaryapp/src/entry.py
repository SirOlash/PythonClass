from datetime import datetime


class Entry:
    def __init__(self, title, content,entry_id):
        self.__title = title
        self.__content = content
        self.__id = entry_id
        self.__date_created = datetime.now().strftime("%H:%M:%S %d-%m-%Y")

    @property
    def get_id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def content(self):
        return self.__content

    @title.setter
    def title(self, title):
        if not title or title.isspace():
            raise ValueError("Title can't be empty")
        self.__title = title

    @content.setter
    def content(self, content):
        if not content or content.isspace():
            raise ValueError("Content can't be empty")
        self.__content = content

    def __str__(self):
        return f"Title: {self.__title}\nContent: {self.__content}\nID: {self.__id}\nDate: {self.__date_created}"

