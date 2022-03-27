class Planet:
    _INVALID_NAME_MESSAGE = "Planet name cannot be empty string or whitespace!"

    def __init__(self, name):
        self.name = name
        self.items = []

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

