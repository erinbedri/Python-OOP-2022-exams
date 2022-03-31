import unittest

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    VALID_NAME = "Test Factory"
    VALID_CAPACITY = 100
    INITIAL_INGREDIENTS = {}
    VALID_INGREDIENTS = ["white", "yellow", "blue", "green", "red"]
    INVALID_INGREDIENT = "dark blue"

    def setUp(self):
        self.paint_factory = PaintFactory(self.VALID_NAME, self.VALID_CAPACITY)

    def test_init(self):
        self.assertEqual(self.VALID_NAME, self.paint_factory.name)
        self.assertEqual(self.VALID_CAPACITY, self.paint_factory.capacity)
        self.assertEqual(self.INITIAL_INGREDIENTS, self.paint_factory.ingredients)
        self.assertEqual(self.VALID_INGREDIENTS, self.paint_factory.valid_ingredients)

    def test_add_ingredient__when_product_type_not_in_valid_ingredients__expect_type_error(self):
        expected = f"Ingredient of type {self.INVALID_INGREDIENT} not allowed in PaintFactory"

        with self.assertRaises(TypeError) as context:
            self.paint_factory.add_ingredient(self.INVALID_INGREDIENT, 100)
        self.assertEqual(expected, str(context.exception))

    def test_add_ingredient__when_capacity_not_enough__expect_value_error(self):
        self.paint_factory.ingredients["white"] = 100

        expected = "Not enough space in factory"

        with self.assertRaises(ValueError) as context:
            self.paint_factory.add_ingredient("white", 100)
        self.assertEqual(expected, str(context.exception))

    def test_add_ingredient__when_capacity_enough_but_product_not_in_ingredients(self):
        expected = {"white": 50}
        self.paint_factory.add_ingredient("white", 50)
        result = self.paint_factory.ingredients
        self.assertEqual(expected, result)

    def test_add_ingredient__when_capacity_enough_product_in_ingredients(self):
        self.paint_factory.ingredients["white"] = 20
        expected = {"white": 70}
        self.paint_factory.add_ingredient("white", 50)
        result = self.paint_factory.ingredients
        self.assertEqual(expected, result)

    def test_remove_ingredient__when_ingredient_not_in_factory__expect_key_error(self):
        expected = 'No such ingredient in the factory'

        with self.assertRaises(Exception) as context:
            self.paint_factory.remove_ingredient(self.INVALID_INGREDIENT, 100)
        self.assertEqual(f"'{expected}'", str(context.exception))

    def test_remove_ingredient__when_ingredient_less_than_zero__expect_value_error(self):
        expected = 'Ingredients quantity cannot be less than zero'

        self.paint_factory.ingredients["white"] = 50

        with self.assertRaises(Exception) as context:
            self.paint_factory.remove_ingredient("white", 100)
        self.assertEqual(expected, str(context.exception))

    def test_remove_ingredient__when_valid(self):
        self.paint_factory.ingredients["white"] = 50
        self.paint_factory.remove_ingredient("white", 10)
        self.assertEqual(40, self.paint_factory.ingredients["white"])

    def test_products_property(self):
        self.paint_factory.ingredients["white"] = 50
        expected = {"white": 50}
        self.assertEqual(expected, self.paint_factory.products)

