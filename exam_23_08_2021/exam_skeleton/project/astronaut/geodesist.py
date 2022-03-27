from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    _INITIAL_OXYGEN_UNITS = 50

    def __init__(self, name):
        super().__init__(name, self._INITIAL_OXYGEN_UNITS)
