from abc import ABC, abstractmethod


class Astronaut(ABC):
    _INVALID_NAME_MESSAGE = "Astronaut name cannot be empty string or whitespace!"
    _OXYGEN_INTAKE_PER_BREATH = 10

    @abstractmethod
    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @classmethod
    def _name_validator(cls, value):
        if not value or not value.strip():
            raise ValueError(cls._INVALID_NAME_MESSAGE)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self._name_validator(value)
        self.__name = value

    def breathe(self):
        self.oxygen -= self._OXYGEN_INTAKE_PER_BREATH

    def increase_oxygen(self, amount):
        self.oxygen += amount

