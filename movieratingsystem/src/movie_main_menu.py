import movies
from movies import Movies


class MovieMenu:

    # def __init__(self):
    #     # movies = Movies()

    def main_menu(self):
        self.main()

    def main(self):
        while True:
            print("""
             Welcome!!! What would you like to do?
                1. Add Movie
                2. Rate A Movie
                3. View Average Rating of a Movie
                4. View Average Rating of all the Movies
                5. Exit
                """)
            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    self.add_movies()
                    break
                case "2":
                    self.rate_a_movie()
                    break
                case "3":
                    self.view_average_rating()
                    break
                case "4":
                    self.total_average_rating()
                    break
                case "5":
                    print("Thanks for Rating!")
                    exit()
                case _: print("Invalid input")

    def add_movies(self):
        movie_name = self.valid_string("Enter Movie Name: ")
        try:
            new_movie = Movies.add_movie(movie_name)
            # Movies.add_movie = movie_name
            # print("Added Movie")
            # movie = Movies.add_movie(movie_name)
            print(f"Movie: {new_movie.movie_title} was added on {new_movie.date_created}")

        except Exception as e:
            print(f"{e}")

        finally:
            self.main()

    def rate_a_movie(self):
        movie_name = self.valid_string("Enter Movie Name: ")
        user_ratings = self.valid_int("Enter your rating: ")
        try:
            Movies.rate_movie(movie_name, user_ratings)
            print("You have successfully rated!")
        except Exception as e:
            print(f"{e}")

        finally:
            self.main()

    def view_average_rating(self):
        movie_name = self.valid_string("Enter the movie Name: ")
        try:
            rate = Movies.view_rating_per_movie(movie_name)
            print(f"The average rating for {movie_name} is {rate}")

        except Exception as e:
            print(f"{e}")

        finally:
            self.main()

    def total_average_rating(self):
        try:
            total_average_rating = Movies.view_total_average_rating()
            print(f"The total average rating is  {total_average_rating}")

        except Exception as e:
            print(f"{e}")

        finally:self.main()





    @staticmethod
    def valid_int(prompt: str):
        while True:
            user_input = int(input(prompt).strip())
            if user_input:
                return user_input
            else:
                print("Please enter a valid integer between 0 and 5")
    @staticmethod
    def valid_string(prompt: str):
        while True:
            user_input = input(prompt).strip()
            if user_input:
                return user_input
            else:
                print("Please enter a valid string")


if __name__ == "__main__":
    movie_menu = MovieMenu()
    movie_menu.main()