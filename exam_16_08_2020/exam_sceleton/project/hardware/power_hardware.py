from math import floor

from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    _TYPE = "Power"
    _CAPACITY_FACTOR = 0.25
    _MEMORY_FACTOR = 1.75

    def __init__(self, name, capacity, memory):
        super().__init__(name,
                         self._TYPE,
                         floor(capacity * self._CAPACITY_FACTOR),
                         floor(memory * self._MEMORY_FACTOR))
