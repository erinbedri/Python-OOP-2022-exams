from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    _GROWN_UPS = 1

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, self._GROWN_UPS)
        self.room_cost = 10
        self.appliances = [TV()]
        self.calculate_expenses(self.appliances)

