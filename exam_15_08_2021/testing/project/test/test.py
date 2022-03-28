import unittest

from project.pet_shop import PetShop


class PetShopTest(unittest.TestCase):
    PET_SHOP_NAME = "Test Shop"
    PET_FOOD_NAME = "Test Food"
    PET_NAME = "Test Pet"
    SECOND_PET_NAME = "Another Pet"

    def setUp(self) -> None:
        self.pet_shop = PetShop(self.PET_SHOP_NAME)

    def test_init(self):
        self.assertEqual(self.PET_SHOP_NAME, self.pet_shop.family_name)
        self.assertDictEqual({}, self.pet_shop.food)
        self.assertListEqual([], self.pet_shop.pets)

    def test_add_food__when_quantity_is_zero__expect_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.pet_shop.add_food(self.PET_FOOD_NAME, 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(context.exception))

    def test_add_food__when_quantity_is_negative__expect_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.pet_shop.add_food(self.PET_FOOD_NAME, -10)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(context.exception))

    def test_add_food__when_food_name_not_in_foods(self):
        quantity = 10
        expected = f"Successfully added {quantity:.2f} grams of {self.PET_FOOD_NAME}."
        result = self.pet_shop.add_food(self.PET_FOOD_NAME, quantity)

        self.assertEqual(quantity, self.pet_shop.food[self.PET_FOOD_NAME])
        self.assertEqual(expected, result)

    def test_add_food__when_food_name_in_foods(self):
        self.pet_shop.food[self.PET_FOOD_NAME] = 50
        quantity = 10
        expected = f"Successfully added {quantity:.2f} grams of {self.PET_FOOD_NAME}."
        result = self.pet_shop.add_food(self.PET_FOOD_NAME, quantity)

        self.assertEqual(quantity + 50, self.pet_shop.food[self.PET_FOOD_NAME])
        self.assertEqual(expected, result)

    def test_add_pet__when_pet_name_not_in_pets__expect_successfully_to_add(self):
        expected = f"Successfully added {self.PET_NAME}."
        result = self.pet_shop.add_pet(self.PET_NAME)

        self.assertEqual([self.PET_NAME], self.pet_shop.pets)
        self.assertEqual(expected, result)

    def test_add_pet__when_pet_name_in_pets__expect_exception(self):
        self.pet_shop.pets = [self.PET_NAME]

        with self.assertRaises(Exception) as context:
            self.pet_shop.add_pet(self.PET_NAME)
        self.assertEqual("Cannot add a pet with the same name", str(context.exception))
        self.assertEqual([self.PET_NAME], self.pet_shop.pets)

    def test_feed_pet__when_pet_not_in_pets__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.pet_shop.feed_pet(self.PET_FOOD_NAME, self.PET_NAME)
        self.assertEqual("Please insert a valid pet name", str(context.exception))

    def test_feed_pet__when_food_not_in_foods__expect_return(self):
        self.pet_shop.pets = [self.PET_NAME]

        expected = f'You do not have {self.PET_FOOD_NAME}'
        result = self.pet_shop.feed_pet(self.PET_FOOD_NAME, self.PET_NAME)

        self.assertEqual(expected, result)

    def test_feed_pet__when_food_less_than_100__expect_return(self):
        self.pet_shop.pets = [self.PET_NAME]
        self.pet_shop.food[self.PET_FOOD_NAME] = 10

        expected = "Adding food..."
        result = self.pet_shop.feed_pet(self.PET_FOOD_NAME, self.PET_NAME)

        self.assertEqual(1010, self.pet_shop.food[self.PET_FOOD_NAME])
        self.assertEqual(expected, result)

    def test_feed_pet__when_valid(self):
        self.pet_shop.pets = [self.PET_NAME]
        self.pet_shop.food[self.PET_FOOD_NAME] = 200

        expected = f"{self.PET_NAME} was successfully fed"
        result = self.pet_shop.feed_pet(self.PET_FOOD_NAME, self.PET_NAME)

        self.assertEqual(100, self.pet_shop.food[self.PET_FOOD_NAME])
        self.assertEqual(expected, result)

    def test_repr__when_no_pets(self):
        expected = f'Shop {self.PET_SHOP_NAME}:\n' \
                   f'Pets: '
        result = repr(self.pet_shop)

        self.assertEqual(expected, result)

    def test_repr__when_one_pet(self):
        self.pet_shop.pets = [self.PET_NAME]

        expected = f'Shop {self.PET_SHOP_NAME}:\n' \
                   f'Pets: {self.PET_NAME}'
        result = repr(self.pet_shop)

        self.assertEqual(expected, result)

    def test_repr__when_two_pets(self):
        self.pet_shop.pets = [self.PET_NAME, self.SECOND_PET_NAME]

        expected = f'Shop {self.PET_SHOP_NAME}:\n' \
                   f'Pets: {self.PET_NAME}, {self.SECOND_PET_NAME}'
        result = repr(self.pet_shop)

        self.assertEqual(expected, result)