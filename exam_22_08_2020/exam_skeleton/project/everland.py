from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total = 0

        for room in self.rooms:
            total += room.expenses
            total += room.room_cost

        return f"Monthly consumption: {total:.2f}$."

    def pay(self):
        result = []

        for room in self.rooms:
            total_expenses = room.expenses + room.room_cost

            if room.budget >= total_expenses:
                room.budget -= total_expenses
                result.append(f"{room.family_name} paid {total_expenses:.2f}$ and have {room.budget:.2f}$ left.")

            else:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)

        return "\n".join(result)

    def status(self):
        result = f"Total population: {sum([room.members_count for room in self.rooms])}\n"

        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count} " \
                      f"members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"

            if room.children:
                for child in room.children:
                    result += f"--- Child {room.children.index(child) + 1} monthly " \
                              f"cost: {child.get_monthly_expense():.2f}$\n"

            if hasattr(room, "appliances"):
                total_expenses = 0
                for app in room.appliances:
                    total_expenses += app.get_monthly_expense()

                result += f"--- Appliances monthly cost: {total_expenses:.2f}$\n"

        return result
