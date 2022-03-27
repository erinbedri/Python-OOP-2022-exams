from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    _OXYGEN_INTAKE_PER_BREATH = 5
    _INITIAL_OXYGEN_UNITS = 70

    def __init__(self, name):
        super().__init__(name, self._INITIAL_OXYGEN_UNITS)

