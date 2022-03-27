from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    _OXYGEN_INTAKE_PER_BREATH = 15
    _INITIAL_OXYGEN_UNITS = 90

    def __init__(self, name):
        super().__init__(name, self._INITIAL_OXYGEN_UNITS)
