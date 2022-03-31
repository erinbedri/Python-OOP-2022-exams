from project.software.software import Software


class ExpressSoftware(Software):
    _TYPE = "Express"
    _MEMORY_CONSUMPTION_FACTOR = 2

    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name,
                         self._TYPE,
                         capacity_consumption,
                         memory_consumption * self._MEMORY_CONSUMPTION_FACTOR)


