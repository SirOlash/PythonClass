import bcrypt


class User:
    def __init__(self, first_name, last_name, email,password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = self.encrypt_password(password)


    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def email(self):
        return self.__email
    
    @staticmethod
    def encrypt_password(normal_password):
        return bcrypt.hashpw(normal_password.encode(),bcrypt.gensalt())

    def verify_password(self, password:str):
        return bcrypt.checkpw(password.encode(), self.__password)



