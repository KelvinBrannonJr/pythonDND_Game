class Player:
    def __init__(self, name):
        self.name = name
        self.player = + 1
        self.health = 100
        self.lives = 3

    def takes_damage(self, damage):
        print(f"{self.name} takes -{damage} HP damage!")

        new_health = self.health - damage
        print(f"{self.name} health {new_health} HP")
        self.__str__()
        return new_health

    def attack(self, atk_amount):
        print(f"{self.name} attacks!")
        self.__str__()
        return atk_amount

    def print(self):
        print(f"Player {self.player} {self.name} is online!\n")
        self.__str__()


sir_kingston = Player("Sir Kingston")
sir_kingston.print()





