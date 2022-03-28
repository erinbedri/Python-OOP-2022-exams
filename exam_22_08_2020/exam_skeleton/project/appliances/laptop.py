from project.appliances.appliance import Appliance


class Laptop(Appliance):
    _COST = 1.0

    def __init__(self):
        super().__init__(self._COST)
