class Child:
    _DAYS_IN_MONTH = 30

    def __init__(self, food_cost: int, *toys_cost):
        self.cost = food_cost + sum(toys_cost)

    def get_monthly_expense(self):
        return self.cost * self._DAYS_IN_MONTH

