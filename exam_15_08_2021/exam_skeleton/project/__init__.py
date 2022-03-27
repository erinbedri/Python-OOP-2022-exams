from project.bakery import Bakery

b = Bakery("Test")
# print(b.add_food("Bread", "Hlqb", 1.25))
# print(b.add_food("Cake", "Torta", 1.5))
#
# print(b.add_drink("Tea", "Chai", 200, "Vnos"))
# print(b.add_drink("Water", "Mineralna", 500, "Butilirana"))
#

print(b.add_table("InsideTable", 25, 6))

print(b.add_table("OutsideTable", 55, 6))
#
# print(b.reserve_table(4))
#
# print(b.order_food(25, "Hlqb", "Torta", "HotDog"))
# print(b.order_drink(55, "Chai", "Chai", "Mineralna", "Cola"))
#
# print(b.get_free_tables_info())
#
# print(b.leave_table(25))
# print(b.get_total_income())

print(b.get_free_tables_info())