from project.car.car import Car


class Driver:
    def __init__(self, name):
        self.name = name
        self.car = None
        self.number_of_wins = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name_is_empty_or_whitespace(value)
        self.__name = value

    @staticmethod
    def __name_is_empty_or_whitespace(value):
        if not value or not value.strip():
            raise ValueError(f"Name should contain at least one character!")

    def change_car(self, car: Car):
        car.is_taken = True
        if self.car is None:
            self.car = car
            return f'Driver {self.name} chose the car {car.model}.'

        self.car.is_taken = False
        old_model = self.car.model
        self.car = car
        return f'Driver {self.name} changed his car from {old_model} to {car.model}.'