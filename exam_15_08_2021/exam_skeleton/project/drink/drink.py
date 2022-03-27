from abc import ABC, abstractmethod


class Drink(ABC):
    @abstractmethod
    def __init__(self, name: str, portion: float, price: float, brand: str):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name_is_empty_or_whitespace(value)
        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        self.__is_zero_or_negative(value)
        self.__portion = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand_is_empty_or_whitespace(value)
        self.__brand = value

    @staticmethod
    def __name_is_empty_or_whitespace(value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty string or white space!")

    @staticmethod
    def __is_zero_or_negative(value):
        if value <= 0:
            raise ValueError("Portion cannot be less than or equal to zero!")

    @staticmethod
    def __brand_is_empty_or_whitespace(value):
        if not value or not value.strip():
            raise ValueError("Brand cannot be empty string or white space!")

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"