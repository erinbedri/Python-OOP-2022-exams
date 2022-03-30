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
