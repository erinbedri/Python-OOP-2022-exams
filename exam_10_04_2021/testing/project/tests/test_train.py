import unittest

from project.train.train import Train


class TrainTests(unittest.TestCase):
    def setUp(self):
        self.train = Train("Test Train", 100)

    def test_init(self):
        self.assertEqual("Test Train", self.train.family_name)
        self.assertEqual(100, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add__when_capacity_is_full(self):
        self.train.capacity = 3
        self.train.passengers = ["Passenger 1", "Passenger 2", "Passenger 3"]

        with self.assertRaises(ValueError) as context:
            self.train.add("Passenger 4")
        self.assertEqual("Train is full", str(context.exception))

    def test_add__when_passenger_in_passengers(self):
        self.train.capacity = 3
        self.train.passengers = ["Passenger 1", "Passenger 2"]

        with self.assertRaises(ValueError) as context:
            self.train.add("Passenger 2")
        self.assertEqual("Passenger Passenger 2 Exists", str(context.exception))

    def test_add__when_valid(self):
        self.train.capacity = 3
        self.train.passengers = ["Passenger 1", "Passenger 2"]

        result = self.train.add("Passenger 3")
        self.assertEqual(["Passenger 1", "Passenger 2", "Passenger 3"], self.train.passengers)
        self.assertEqual("Added passenger Passenger 3", result)

    def test_remove__when_passenger_not_in_passengers(self):
        self.train.passengers = ["Passenger 1", "Passenger 2", "Passenger 3"]

        with self.assertRaises(ValueError) as context:
            self.train.remove("Passenger 4")
        self.assertEqual("Passenger Not Found", str(context.exception))

    def test_remove__when_valid(self):
        self.train.passengers = ["Passenger 1", "Passenger 2", "Passenger 3"]

        result = self.train.remove("Passenger 3")
        self.assertEqual(["Passenger 1", "Passenger 2"], self.train.passengers)
        self.assertEqual("Removed Passenger 3", result)