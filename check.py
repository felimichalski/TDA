class Player:
    def __init__(self, name: str, attack: int, defense: int):
        self.name: str = name
        self.attack: int = attack
        self.defense: int = defense


class OptimizedFormation:
    def __init__(self, players: list[Player]):
        self.attackers: list[Player] = []
        self.defenders: list[Player] = []
        self.attacking_value: int = 0
        self.defending_value: int = 0
        self.best_attackers: list[Player] = self.__retrieve_best_attackers(players)
        self.__optimize(players, self.attackers, self.defenders, self.attacking_value, self.defending_value, 0)

    def __optimize(self, players, current_attackers, current_defenders, attacking_value, defending_value, index):
        if len(current_attackers) < 5 and players[index] in self.best_attackers:
            # Include current player in attackers
            current_attackers.append(players[index])
            self.__optimize(players, current_attackers, current_defenders, attacking_value + players[index].attack, defending_value, index + 1)
        elif len(current_defenders) < 5:
            # Include current player in defenders
            current_defenders.append(players[index])
            self.__optimize(players, current_attackers, current_defenders, attacking_value, defending_value + players[index].defense, index + 1)
        else:
            # Valid solution
            self.attacking_value = attacking_value
            self.defending_value = defending_value
            self.attackers = current_attackers
            self.defenders = current_defenders

    def __optimize_longer(self, players, current_attackers, current_defenders, attacking_value, defending_value, index):
        if index == 10:
            if (attacking_value > self.attacking_value
                    or (attacking_value == self.attacking_value and defending_value > self.defending_value)
                    or (attacking_value == self.attacking_value and defending_value == self.defending_value
                        and self.__attackers_lexicographically_earlier(current_attackers))):
                # Valid solution
                self.attacking_value = attacking_value
                self.defending_value = defending_value
                self.attackers = current_attackers
                self.defenders = current_defenders
            return

        if len(current_attackers) < 5:
            # Include current player in attackers
            current_attackers.append(players[index])
            self.__optimize(players, current_attackers, current_defenders, attacking_value + players[index].attack, defending_value, index + 1)
            current_attackers.pop()

        if len(current_defenders) < 5:
            # Include current player in defenders
            current_defenders.append(players[index])
            self.__optimize(players, current_attackers, current_defenders, attacking_value, defending_value + players[index].defense, index + 1)
            current_defenders.pop()

    def __attackers_lexicographically_earlier(self, attackers) -> bool:
        for a1, a2 in zip(attackers, self.attackers):
            if a1.name < a2.name:
                return True
            elif a1.name > a2.name:
                return False
        return False

    def __retrieve_best_attackers(self, players) -> list[Player]:
        copy: list[Player] = players[:]
        # Sort players by highest attack, then by lowest defense, and finally lexicographically.
        copy.sort(key=lambda x: (-x.attack, x.defense, x.name))
        return copy[:5]


def solve_problem():
    number_of_cases: int = int(input("Enter the data in the requested format:"))

    # Read all cases first
    test_cases: list[list[Player]] = []
    for _ in range(number_of_cases):
        players: list[Player] = []
        for _ in range(10):
            # Destructure player info and create a Player
            name, attack, defense = input().split()
            players.append(Player(name, int(attack), int(defense)))
        test_cases.append(players)

    # Process each case
    for t, players in enumerate(test_cases):
        optimized_formation = OptimizedFormation(players)

        print("Case " + str(t + 1) + ":")
        print_information(optimized_formation.attackers)
        print_information(optimized_formation.defenders)


def print_information(players: list[Player]):
    # Sort the list of players alphabetically
    players.sort(key=lambda x: x.name)
    print("(" + ", ".join(player.name for player in players) + ")")


# Used to run the program from Intellij IDEA
# if __name__ == '__main__':
#     solve_problem()
solve_problem()
