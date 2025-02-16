from calendar import month
from datetime import datetime


class Human:
    def __init__(self, name, date_of_birth:str,gender,height):
        self._name = name
        self._date_of_birth = date_of_birth
        self._gender = gender
        self._height = height

    def get_age(self):
       #day, month, year = map(int, self._date_of_birth.split('-'))
       # day, month,year = self,_date_of_birth.split('-')
        current_year = datetime.now().year
