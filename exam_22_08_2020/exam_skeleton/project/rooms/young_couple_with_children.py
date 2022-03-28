from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    _GROWN_UPS = 2

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_one + salary_two, self._GROWN_UPS + len(children))
        self.room_cost = 30
        self.children = list(children)
        self.appliances = [TV(), Fridge(), Laptop()] * self._GROWN_UPS * len(self.children) \
            if self.children else [TV(), Fridge(), Laptop()] * self._GROWN_UPS
        self.calculate_expenses(self.appliances, self.children)

