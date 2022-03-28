from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    _GROWN_UPS = 2

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, pension_one + pension_two, self._GROWN_UPS)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove()] * self._GROWN_UPS
        self.calculate_expenses(self.appliances)
