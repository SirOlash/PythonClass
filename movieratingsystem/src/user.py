class User:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    @property
    def name(self):
        return self.user_name


