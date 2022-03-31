from math import floor

from project.software.software import Software


class LightSoftware(Software):
    _TYPE = "Light"
    _CAPACITY_CONSUMPTION_FACTOR = 1.5
    _MEMORY_CONSUMPTION_FACTOR = 0.5

    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name,
                         self._TYPE,
                         (floor(capacity_consumption * self._CAPACITY_CONSUMPTION_FACTOR)),
                         floor(memory_consumption * self._MEMORY_CONSUMPTION_FACTOR))


