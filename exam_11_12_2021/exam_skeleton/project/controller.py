from project.core.car_factory import CarFactory
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

        self.car_factory = CarFactory()

    def create_car(self, car_type: str, model: str, speed_limit: int):
        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")

        try:
            car = self.car_factory.create_car(car_type, model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

        except RuntimeError:
            pass

    def create_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

        driver = self.__create_drive_by_name(driver_name)

        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")

        race = self.__create_race_by_name(race_name)

        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__get_driver_by_name(driver_name)

        car = self.__get_last_free_car_by_type(car_type)

        return driver.change_car(car)

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__get_race_by_name(race_name)

        driver = self.__get_driver_by_name(driver_name)

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__get_race_by_name(race_name)

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        fastest_cars = sorted([(driver, driver.car.speed_limit) for driver in race.drivers],
                                   key=lambda kwp: -kwp[1])

        result = ""
        for driver, speed in fastest_cars[:3]:
            driver.number_of_wins += 1
            result += f"Driver {driver.name} wins the {race_name} race with a speed of {speed}.\n"

        return result.strip()

    @staticmethod
    def __create_drive_by_name(driver_name):
        return Driver(driver_name)

    @staticmethod
    def __create_race_by_name(race_name):
        return Race(race_name)

    def __get_last_free_car_by_type(self, car_type):
        for idx in range(len(self.cars) - 1, -1, -1):
            car = self.cars[idx]

            if not car.is_taken and car.__class__.__name__ == car_type:
                return car

        raise Exception(f'Car {car_type} could not be found!')

    def __get_driver_by_name(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver

        raise Exception(f'Driver {driver_name} could not be found!')

    def __get_race_by_name(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race

        raise Exception(f'Race {race_name} could not be found!')
