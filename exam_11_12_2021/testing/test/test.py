import unittest

from project.team import Team


class TestTeam(unittest.TestCase):
    FIRST_VALID_TEAM_NAME = "Test"
    SECOND_VALID_TEAM_NAME = "Example"
    INVALID_TEAM_NAME = "123"

    ERROR_MESSAGE_INVALID_NAME = "Team Name can contain only letters!"

    def setUp(self):
        self.team = Team(self.FIRST_VALID_TEAM_NAME)
        self.second_team = Team(self.SECOND_VALID_TEAM_NAME)

    def test_init(self):
        self.assertEqual(self.FIRST_VALID_TEAM_NAME, self.team.name)
        self.assertEqual({}, self.team.members)

    def test_init__when_name_not_valid__expect_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.another_team = Team(self.INVALID_TEAM_NAME)
        self.assertEqual(self.ERROR_MESSAGE_INVALID_NAME, str(context.exception))

    def test_name_setter__when_name_not_alpha__expect_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.team.name = self.INVALID_TEAM_NAME
        self.assertEqual(self.ERROR_MESSAGE_INVALID_NAME, str(context.exception))

    def test_add_members_adds_only_new_members(self):
        self.team.members["Erin"] = 28

        result = self.team.add_member(Erin=28, Emre=18, Irena=28)

        self.assertEqual("Successfully added: Emre, Irena", result)
        self.assertEqual(18, self.team.members["Emre"])
        self.assertEqual(28, self.team.members["Irena"])

    # def test_add_member__when_no_member(self):
    #     expected = "Successfully added: "
    #     result = self.team.add_member()
    #
    #     self.assertEqual({}, self.team.members)
    #     self.assertEqual(expected, result)
    #
    # def test_add_member__when_member_exists(self):
    #     self.team.members = {"Erin": 28}
    #
    #     expected = "Successfully added: "
    #     result = self.team.add_member(Erin=28)
    #
    #     self.assertEqual({"Erin": 28}, self.team.members)
    #     self.assertEqual(expected, result)
    #
    # def test_add_member__when_single_member(self):
    #     expected = "Successfully added: Erin"
    #     result = self.team.add_member(Erin=28)
    #
    #     self.assertEqual({'Erin': 28}, self.team.members)
    #     self.assertEqual(expected, result)
    #
    # def test_add_member__when_multiple_members(self):
    #     expected = "Successfully added: Erin, Sanjeev"
    #     result = self.team.add_member(Erin=28, Sanjeev=27)
    #
    #     self.assertEqual(28, self.team.members["Erin"])
    #     self.assertEqual(27, self.team.members["Sanjeev"])
    #     self.assertEqual(expected, result)

    def test_remove_member__when_user_not_member(self):
        expected = "Member with name Erin does not exist"
        result = self.team.remove_member("Erin")

        self.assertEqual({}, self.team.members)
        self.assertEqual(expected, result)

    def test_remove_member__when_user_is_member(self):
        self.team.members = {"Erin": 28}

        expected = "Member Erin removed"
        result = self.team.remove_member("Erin")
        self.assertEqual({}, self.team.members)
        self.assertEqual(expected, result)

    def test_gt__when_true(self):
        self.team.members = {"Erin": 28, "Sanjeev": 27}
        self.second_team.members = {"Albert": 27}

        expected = True
        result = self.team > self.second_team
        self.assertEqual(expected, result)

    def test_gt__when_false(self):
        self.team.members = {"Erin": 28, "Sanjeev": 27}
        self.second_team.members = {"Albert": 27}

        expected = False
        result = self.team < self.second_team
        self.assertEqual(expected, result)

    def test_len(self):
        self.team.members = {"Erin": 28, "Sanjeev": 27}

        expected = 2
        result = len(self.team)
        self.assertEqual(expected, result)

    def test_add(self):
        self.team.members = {"Erin": 28}
        self.second_team.members = {"Albert": 27}

        result = self.team + self.second_team
        self.assertEqual("TestExample", result.name)
        self.assertEqual({"Erin": 28, "Albert": 27}, result.members)

    def test_str(self):
        self.team.members = {"Erin": 28, "Albert": 27}
        expected = "Team name: Test\n" \
                   "Member: Erin - 28-years old\n" \
                   "Member: Albert - 27-years old"

        result = str(self.team)
        self.assertEqual(expected, result)
