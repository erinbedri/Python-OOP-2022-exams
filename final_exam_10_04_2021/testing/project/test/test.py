import unittest

from project.movie import Movie


class MovieTest(unittest.TestCase):
    VALID_NAME = "Gladiator"
    VALID_YEAR = 2000
    VALID_RATING = 8.5
    VALID_ACTOR = "Russel Crowe"
    SECOND_VALID_ACTOR = "Dimitar Gyurchev"

    def setUp(self) -> None:
        self.valid_movie = Movie(self.VALID_NAME, self.VALID_YEAR, self.VALID_RATING)

    def test_init(self):
        self.assertEqual(self.VALID_NAME, self.valid_movie.name)
        self.assertEqual(self.VALID_YEAR, self.valid_movie.year)
        self.assertEqual(self.VALID_RATING, self.valid_movie.rating)
        self.assertEqual([], self.valid_movie.actors)

    def test_name_setter__when_name_empty_string__expect_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(context.exception))

    def test_year_setter__when_year_is_less_than_1887__expect_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie.year = 1886
        self.assertEqual("Year is not valid!", str(context.exception))

    def test_add_actor__when_actor_already_in_actors__expect_return(self):
        self.valid_movie.actors = [self.VALID_ACTOR]

        expected = f"{self.VALID_ACTOR} is already added in the list of actors!"
        result = self.valid_movie.add_actor(self.VALID_ACTOR)

        self.assertEqual(expected, result)

    def test_add_actor__when_actor_not_in_actors(self):
        self.valid_movie.add_actor("Erin Bedri")

        self.assertEqual(["Erin Bedri"], self.valid_movie.actors)

    def test_gt(self):
        other_movie = Movie("Tzar", 2010, 6)

        self.assertEqual(f'"{self.valid_movie.name}" is better than "{other_movie.name}"', self.valid_movie > other_movie)
        self.assertEqual(f'"{self.valid_movie.name}" is better than "{other_movie.name}"', self.valid_movie < other_movie)

    def test_repr(self):
        self.valid_movie.actors = [self.VALID_ACTOR, self.SECOND_VALID_ACTOR]

        expected = f"Name: {self.VALID_NAME}\n" \
                   f"Year of Release: {self.VALID_YEAR}\n" \
                   f"Rating: {self.VALID_RATING:.2f}\n" \
                   f"Cast: {self.VALID_ACTOR}, {self.SECOND_VALID_ACTOR}"

        result = repr(self.valid_movie)

        self.assertEqual(expected, result)