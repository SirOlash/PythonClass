from datetime import datetime



class Movie:
    def __init__(self, movie_title):
        self.__movie_title = movie_title
        self.__average_rating = None
        self.__date_created = datetime.now().strftime("%H:%M:%S %d-%m-%Y")

    @property
    def movie_rating(self):
        return self.__average_rating

    @movie_rating.setter
    def movie_rating(self, rating):
        if self.__average_rating is None:
            self.__average_rating = rating

        else:
            self.__average_rating = (self.__average_rating + rating) / 2

    @property
    def movie_title(self):
        return self.__movie_title

    @property
    def date_created(self):
        return self.__date_created

