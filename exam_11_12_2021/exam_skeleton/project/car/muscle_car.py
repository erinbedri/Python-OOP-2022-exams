from project.car.car import Car


class MuscleCar(Car):
    _MIN = 250
    _MAX = 450

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if not self._MIN < value < self._MAX:
            raise ValueError(f"Invalid speed limit! Must be between {self._MIN} and {self._MAX}!")
        self.__speed_limit = value

    @property
    def type(self):
        return "MuscleCar"
