from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.food = set()
        self.drinks_menu = []
        self.drinks = set()
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name_is_empty_or_whitespace(value)
        self.__name = value

    @staticmethod
    def __name_is_empty_or_whitespace(value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty string or white space!")

    def add_food(self, food_type: str, name: str, price: float):
        for food in self.food_menu:
            if food.family_name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")

        food = self.__create_food(food_type, name, price)

        if food:
            self.food_menu.append(food)
            self.food.add(food.family_name)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        for drink in self.drinks_menu:
            if drink.family_name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        drink = self.__create_drink(drink_type, name, portion, brand)

        if drink:
            self.drinks_menu.append(drink)
            self.drinks.add(drink.family_name)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        for table in self.tables_repository:
            if table.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        table = self.__create_table(table_type, table_number, capacity)

        if table:
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table = self.__get_free_table(number_of_people)

        if table:
            table.reserve(number_of_people)
            return f"Table {table.table_number} has been reserved for {number_of_people} people"
        else:
            return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names: str):
        table = self.__get_table_by_table_number(table_number)

        if not table:
            return f"Could not find table {table_number}"

        food_that_can_be_ordered_str = [f for f in food_names if f in self.food]
        food_that_cannot_be_ordered_str = [f for f in food_names if f not in self.food]

        foods = [self.__get_food_by_name(food_name) for food_name in food_that_can_be_ordered_str]
        [table.order_food(f) for f in foods]

        print_out = f"Table {table_number} ordered:\n"
        print_out += '\n'.join([repr(f) for f in foods])
        print_out += f"\n{self.name} does not have in the menu:\n"
        print_out += '\n'.join([f for f in food_that_cannot_be_ordered_str])

        return print_out

    def order_drink(self, table_number: int, *drink_names: str):
        table = self.__get_table_by_table_number(table_number)

        if not table:
            return f"Could not find table {table_number}"

        drinks_that_can_be_ordered_str = [d for d in drink_names if d in self.drinks]
        drinks_that_cannot_be_ordered_str = [d for d in drink_names if d not in self.drinks]

        drinks = [self.__get_drink_by_name(drink_name) for drink_name in drinks_that_can_be_ordered_str]
        [table.order_drink(d) for d in drinks]

        print_out = f"Table {table_number} ordered:\n"
        print_out += '\n'.join([repr(d) for d in drinks])
        print_out += f"\n{self.name} does not have in the menu:\n"
        print_out += '\n'.join([d for d in drinks_that_cannot_be_ordered_str])

        return print_out

    def leave_table(self, table_number: int):
        table = self.__get_table_by_table_number(table_number)
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f"Table: {table_number}\n" \
               f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        tables_info = ""
        for table in self.tables_repository:
            if not table.is_reserved:
                tables_info += table.free_table_info()
        return tables_info.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    @staticmethod
    def __create_food(food_type, name, price):
        if food_type == "Bread":
            return Bread(name, price)
        elif food_type == "Cake":
            return Cake(name, price)

    @staticmethod
    def __create_drink(drink_type, name, portion, brand):
        if drink_type == "Tea":
            return Tea(name, portion, brand)
        elif drink_type == "Water":
            return Water(name, portion, brand)

    @staticmethod
    def __create_table(table_type, table_number, capacity):
        if table_type == "InsideTable":
            return InsideTable(table_number, capacity)
        elif table_type == "OutsideTable":
            return OutsideTable(table_number, capacity)

    def __get_free_table(self, number_of_people):
        for table in self.tables_repository:
            if table.capacity >= number_of_people and not table.is_reserved:
                return table

    def __get_table_by_table_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

    def __get_food_by_name(self, food_name):
        foods = [f for f in self.food_menu if f.family_name == food_name]
        return foods[0] if foods else None

    def __get_drink_by_name(self, drink_name):
        drinks = [d for d in self.drinks_menu if d.family_name == drink_name]
        return drinks[0] if drinks else None
