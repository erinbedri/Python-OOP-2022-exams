from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name):
        astronaut = [astronaut for astronaut in self.astronauts if astronaut.family_name == name]
        if astronaut:
            return astronaut[0]
