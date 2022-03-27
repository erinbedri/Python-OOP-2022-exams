from abc import ABC, abstractmethod


class BakedFood(ABC):
    @abstractmethod
    def __init__(self, name: str, portion: float, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__is_empty_or_whitespace(value)
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__is_zero_or_negative(value)
        self.__price = value

    @staticmethod
    def __is_empty_or_whitespace(value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty string or white space!")

    @staticmethod
    def __is_zero_or_negative(value):
        if value <= 0:
            raise ValueError("Price cannot be less than or equal to zero!")

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"

