from collections import deque

from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    _OXYGEN_INCREASE = 10
    _MIN_OXYGEN_LIMIT_FOR_MISSION = 30

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.unsuccessful_missions = 0

    @staticmethod
    def _create_astronaut(astronaut_type, name):
        if astronaut_type == "Biologist":
            return Biologist(name)
        elif astronaut_type == "Geodesist":
            return Geodesist(name)
        elif astronaut_type == "Meteorologist":
            return Meteorologist(name)
        raise Exception("Astronaut type is not valid!")

    @staticmethod
    def _create_planet(name, items):
        items_lst = items.split(", ")
        planet = Planet(name)
        planet.items.extend(items_lst)
        return planet

    def add_astronaut(self, astronaut_type, name):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        new_astronaut = self._create_astronaut(astronaut_type, name)
        self.astronaut_repository.astronauts.append(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name, items):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        new_planet = self._create_planet(name, items)
        self.planet_repository.planets.append(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        astronaut = self.astronaut_repository.find_by_name(name)

        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.astronauts.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        [astronaut.increase_oxygen(self._OXYGEN_INCREASE) for astronaut in self.astronaut_repository.astronauts]

    def send_on_mission(self, planet_name):
        planet = self.planet_repository.find_by_name(planet_name)

        if not planet:
            raise Exception("Invalid planet name!")

        astronauts = [astronaut for astronaut in self.astronaut_repository.astronauts
                      if astronaut.oxygen > self._MIN_OXYGEN_LIMIT_FOR_MISSION]

        if not astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        sorted_astronaut_lst = sorted(astronauts, key=lambda x: x.oxygen, reverse=True)

        if len(sorted_astronaut_lst) > 5:
            suitable_astronauts = deque(sorted_astronaut_lst[:5])
        else:
            suitable_astronauts = deque(sorted_astronaut_lst)

        astronauts_into_space = set()
        items_collected = 0

        while suitable_astronauts and planet.items:
            current_astronaut = suitable_astronauts.popleft()
            astronauts_into_space.add(current_astronaut)

            current_item = planet.items.pop()

            current_astronaut.breathe()
            current_astronaut.backpack.append(current_item)
            items_collected += 1

            if current_astronaut.oxygen <= 0:
                continue
            else:
                suitable_astronauts.appendleft(current_astronaut)

        if len(planet.items) > 0:
            self.unsuccessful_missions += 1
            return "Mission is not completed."
        else:
            self.successful_missions += 1
            return f"Planet: {planet_name} was explored. {len(astronauts_into_space)} astronauts " \
                   f"participated in collecting items."

    def report(self):
        report = f"{self.successful_missions} successful missions!\n"
        report += f"{self.unsuccessful_missions} missions were not completed!\n"
        report += "Astronauts' info:\n"

        for astronaut in self.astronaut_repository.astronauts:
            report += f"Name: {astronaut.name}\n"
            report += f"Oxygen: {astronaut.oxygen}\n"
            if astronaut.backpack:
                report += f"Backpack items: {', '.join([item for item in astronaut.backpack])}\n"
            else:
                report += "Backpack items: none\n"

        return report








