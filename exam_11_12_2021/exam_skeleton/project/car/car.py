from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, model, speed_limit):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit.limit

    @speed_limit.setter
    def speed_limit(self, value):
        self.__validate_speed_limit(value)
        self.__speed_limit = value

    def __validate_speed_limit(self, value):
        if value < self.min_speed_limit or value > self.max_speed_limit:
            raise ValueError(f"Invalid speed limit! Must be between {self.min_speed_limit} "
                             f"and {self.max_speed_limit}!")

    @property
    @abstractmethod
    def min_speed_limit(self):
        pass

    @property
    @abstractmethod
    def max_speed_limit(self):
        pass

