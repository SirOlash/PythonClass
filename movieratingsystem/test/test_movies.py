import unittest

from movies import Movies


class MyTestCase(unittest.TestCase):
    def setUp(self):
        Movies.movie_list = []


    def test_that_you_can_add_movie(self):
        new_movie = Movies.add_movie("friends")
        self.assertEqual(len(Movies.movie_list), 1)
        self.assertEqual(new_movie.movie_title, "friends")


    def test_that_you_can_add_more_than_one_movie(self):
        Movies.add_movie("friends")
        self.assertEqual(len(Movies.movie_list), 1)
        new_movie = Movies.add_movie("Big bang")
        self.assertEqual(len(Movies.movie_list), 2)
        self.assertEqual(new_movie.movie_title, "Big bang")

    def test_that_you_cannot_add_same_movie_twice(self):
        Movies.add_movie("friends")
        self.assertEqual(len(Movies.movie_list), 1)
        with self.assertRaises(Exception) as context:
            Movies.add_movie("friends")

        self.assertEqual(str(context.exception), "Movie friends already exists")



    def test_that_you_can_rate_movies(self):
        new_movie = Movies.add_movie("friends")
        self.assertEqual(new_movie.movie_rating,None)
        rated_movie = Movies.rate_movie("friends",5)
        self.assertEqual(rated_movie.movie_rating, 5)

    def test_that_you_cannot_rate_above_5_and_below_0(self):
        Movies.add_movie("friends")

        with self.assertRaises(Exception) as context:
            Movies.rate_movie("friends",6)

        self.assertEqual(str(context.exception), "Rating must be between 0 and 5")





    def test_that_error_is_thrown_when_you_try_to_rate_a_movie_that_is_not_added_yet(self):
        with self.assertRaises(Exception) as context:
            Movies.rate_movie("friends",4)

        self.assertEqual(str(context.exception), "Movie not found")

    def test_that_you_can_view_total_average_rating(self):
        Movies.add_movie("friends")
        Movies.add_movie("Big bang")
        Movies.rate_movie("friends", 2)
        Movies.rate_movie("Big bang", 4)
        self.assertEqual(Movies.view_total_average_rating(), 3)


        # self.assertEqual(len(Movies.movie_list), 1)

    def test_that_exception_is_thrown_if_no_course_is_added_and_you_try_to_view_total_rating(self):
        with self.assertRaises(Exception) as context:
            Movies.view_total_average_rating()

        self.assertEqual(str(context.exception), "No movies found")


    def test_that_you_can_view_rating_per_movie(self):
        Movies.add_movie("friends")
        Movies.rate_movie("friends", 2)
        Movies.rate_movie("friends", 4)
        rated_movie = Movies.view_rating_per_movie("friends")
        self.assertEqual(rated_movie, 3)

    def test_that_exception_is_thrown_if_no_course_is_found_while_trying_to_view_rating(self):
        with self.assertRaises(Exception) as context:
            Movies.view_rating_per_movie("friends")

        self.assertEqual(str(context.exception), "Movie not found")






if __name__ == '__main__':
    unittest.main()
