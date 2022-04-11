class Controller:
    _SUSTENANCE_TYPES = ["Food", "Drink"]

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        players_added = []

        for player in players:
            if player not in self.players:
                players_added.append(player.name)
                self.players.append(player)

        return f"Successfully added: {', '.join(players_added)}"

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type not in self._SUSTENANCE_TYPES:
            return

        player = self.__get_player_by_name(player_name)
        if player is None:
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        supply = self.__get_last_supply_by_type(sustenance_type)

        self.supplies.remove(supply)

        if player.stamina + supply.energy < 100:
            player.stamina += supply.energy
        else:
            player.stamina = 100

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        cannot_participate = []
        player_one = self.__get_player_by_name(first_player_name)
        player_two = self.__get_player_by_name(second_player_name)

        if player_one.stamina == 0 or player_two.stamina == 0:
            if player_one.stamina == 0:
                cannot_participate.append(f"Player {player_one.name} does not have enough stamina.")
            if player_two.stamina == 0:
                cannot_participate.append(f"Player {player_two.name} does not have enough stamina.")
            return f'\n'.join(cannot_participate)

        first_attacker = player_one if player_two.stamina > player_one.stamina else player_two
        second_attacker = player_one if player_two.stamina < player_one.stamina else player_two

        second_attacker.stamina -= first_attacker.stamina / 2
        if second_attacker.stamina <= 0:
            second_attacker.stamina = 0
            return f"Winner: {first_attacker.name}"

        first_attacker.stamina -= second_attacker.stamina / 2
        if first_attacker.stamina <= 0:
            first_attacker.stamina = 0
            return f"Winner: {second_attacker.name}"

        if first_attacker.stamina > second_attacker.stamina:
            return f"Winner: {first_attacker.name}"
        else:
            return f"Winner: {second_attacker.name}"

    def next_day(self):
        for player in self.players:

            if (player.stamina - player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= (player.age * 2)

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []

        for player in self.players:
            result.append(str(player))

        for supply in self.supplies:
            result.append(supply.details())

        return '\n'.join(result)

    def __get_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def __get_last_supply_by_type(self, sustenance_type):
        supplies = []

        for supply in self.supplies:
            if supply.__class__.__name__ == sustenance_type:
                supplies.append(supply)

        if len(supplies) == 0:
            if sustenance_type == "Food":
                return "There are no food supplies left!"
            elif sustenance_type == "Drink":
                return "There are no drink supplies left!"

        return supplies[-1]
