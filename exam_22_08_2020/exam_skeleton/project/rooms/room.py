class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        self.__validate_expenses(value)
        self.__expenses = value

    @staticmethod
    def __validate_expenses(value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")

    def calculate_expenses(self, *args):
        total_cost = 0
        for arg in args:
            for el in arg:
                total_cost += el.get_monthly_expense()

        self.expenses = total_cost

