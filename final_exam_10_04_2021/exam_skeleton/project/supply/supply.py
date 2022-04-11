from abc import ABC, abstractmethod


class Supply(ABC):
    _IS_EMPTY_OR_WHITESPACE_ERROR_MESSAGE = "Name cannot be an empty string."
    _IS_NEGATIVE_ERROR_MESSAGE = "Energy cannot be less than zero."

    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__is_empty_or_whitespace(value)
        self.__name = value

    @classmethod
    def __is_empty_or_whitespace(cls, value):
        if not value or not value.strip():
            raise ValueError(cls._IS_EMPTY_OR_WHITESPACE_ERROR_MESSAGE)

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        self.__is_negative(value)
        self.__energy = value

    @classmethod
    def __is_negative(cls, value):
        if value < 0:
            raise ValueError(cls._IS_NEGATIVE_ERROR_MESSAGE)

    @abstractmethod
    def details(self):
        pass

