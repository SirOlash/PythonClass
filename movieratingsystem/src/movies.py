
from movie import Movie


class Movies:
    movie_list = []

    @classmethod
    def add_movie(cls, movie_name):
        for movie in cls.movie_list:
            if movie.movie_title.lower().strip() == movie_name.lower().strip():
                raise ValueError(f"Movie {movie.movie_title} already exists")

        new_movie = Movie(movie_name)
        cls.movie_list.append(new_movie)
        return new_movie


    @classmethod
    def rate_movie(cls,movie_name,ratings:float):
        # selected_movie = None
        if ratings < 0 or ratings > 5:
            raise ValueError("Rating must be between 0 and 5")
        for movie in cls.movie_list:
            if movie.movie_title.lower().strip() == movie_name.lower().strip():
                # movie.movie_rating(user_ratings)
                movie.movie_rating= ratings
                return movie
                # selected_movie = movie.movie_rating(user_rating)
                # selected_movie.
                # return selected_movie

        raise Exception("Movie not found")

    @classmethod
    def view_rating_per_movie(cls,movie_name):
        for movie in cls.movie_list:
            if movie.movie_title.lower().strip() == movie_name.lower().strip():
                return movie.movie_rating

        raise Exception("Movie not found")

    @classmethod
    def view_total_average_rating(cls):
        if len(cls.movie_list) == 0:
            raise Exception("No movies found")

        average_rating = 0
        for movie in cls.movie_list:
            average_rating += movie.movie_rating

        total_average_rating = average_rating / len(cls.movie_list)
        return total_average_rating






