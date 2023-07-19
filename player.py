class Player:
    def __init__(self, name):
        self.name = name
        self.player = + 1
        self.health = 100
        self.lives = 3

    def get_health(self):
        return self.health

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

    def death(self):
        if self.health <= 0:
            print(f"{self.name} has died..")
        return

    def print(self):
        print(f"Player {self.player} {self.name} is online!\n")
        self.__str__()







