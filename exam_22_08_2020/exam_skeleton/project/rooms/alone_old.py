from project.rooms.room import Room


class AloneOld(Room):
    _GROWN_UPS = 1

    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, pension, self._GROWN_UPS)
        self.room_cost = 10

