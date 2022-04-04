class Race:
    def __init__(self, name):
        self.name = name
        self.drivers = []

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
            raise ValueError("Name cannot be an empty string!")
