from project.rooms.alone_old import AloneOld
from project.rooms.alone_young import AloneYoung
from project.rooms.old_couple import OldCouple
from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren
from project.people.child import Child
from project.everland import Everland

everland = Everland()

def test_one():
    alone_old = AloneOld("Flintstones", 100)
    alone_young = AloneYoung("Testovi", 150)
    old_couple = OldCouple("Durtite", 150, 100)
    young_couple = YoungCouple("Johnsons", 150, 205)
    #
    # child1 = Child(5, 1, 2, 1)
    # child2 = Child(3, 2)
    young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520)

    # everland.add_room(old_couple)
    everland.add_room(young_couple)
    everland.add_room(young_couple_with_children)

    print(everland.get_monthly_consumptions())
    print(everland.pay())
    print(everland.status())


if __name__ == "__main__":
    test_one()
