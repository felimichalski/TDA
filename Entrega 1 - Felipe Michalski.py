class Player:
    def __init__(self, name: str, attack: int, defense: int):
        self.name: str = name
        self.attack: int = attack
        self.defense: int = defense


class OptimizedFormation:
    def __init__(self, players: list[Player]):
        self.attackers: list[Player] = []
        self.defenders: list[Player] = []
        self.__optimize(players, [], 0)

    def __optimize(self, players, current_attackers, index):
        if len(current_attackers) == 5:
            current_defenders: list[Player] = [player for player in players if player not in current_attackers]

            current_attacking_value: int = self.__retrieve_attacking_value(current_attackers)
            current_defending_value: int = self.__retrieve_defending_value(current_defenders)

            best_attacking_value: int = self.__retrieve_attacking_value(self.attackers)
            best_defending_value: int = self.__retrieve_defending_value(self.defenders)

            if (len(self.attackers) == 0
                    or current_attacking_value > best_attacking_value
                    or (current_attacking_value == best_attacking_value
                        and current_defending_value > best_defending_value)
                    or (current_attacking_value == best_attacking_value
                        and current_defending_value == best_defending_value
                        and self.__attackers_lexicographically_earlier(current_attackers))):
                # Valid solution, shallow copy to prevent modification by reference
                self.attackers = current_attackers[:]
                self.defenders = current_defenders[:]
            return
        if len(players) == index:
            return

        self.__optimize(players, current_attackers + [players[index]], index + 1)
        self.__optimize(players, current_attackers, index + 1)

    def __retrieve_attacking_value(self, players: list[Player]) -> int:
        return sum(player.attack for player in players)

    def __retrieve_defending_value(self, players: list[Player]) -> int:
        return sum(player.defense for player in players)

    def __attackers_lexicographically_earlier(self, attackers: list[Player]) -> bool:
        for i, player in enumerate(attackers):
            if self.attackers[i].name > player.name:
                return True
            elif self.attackers[i].name < player.name:
                return False
        return False

def solve_problem():
    number_of_cases: int = int(input())
    answer: list[str] = []

    # Read all cases first
    for i in range(number_of_cases):
        players: list[Player] = []
        for _ in range(10):
            # Destructure player info and create a Player
            name, attack, defense = input().split()
            players.append(Player(name, int(attack), int(defense)))

        optimized_formation = OptimizedFormation(players)

        answer.append("Case " + str(i + 1) + ":")
        answer.append(parse_information(optimized_formation.attackers))
        answer.append(parse_information(optimized_formation.defenders))
    print("\n".join(answer))


def parse_information(players: list[Player]) -> str:
    return "(" + ", ".join(sorted(player.name for player in players)) + ")"


if __name__ == '__main__':
    solve_problem()
