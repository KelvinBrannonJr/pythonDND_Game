"""
OBJECTIVE
- Add mechanic to allow player attacks to randomly miss
- Add random range indexer for attack damage
"""


class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.player = + 1
        self.health = 100
        self.lives = 3
        self.player_queue_number = 1
        self.player_turn = False

    def get_health(self):
        print(self.health)
        return self.health

    def takes_damage(self, damage):
        if damage > 0:
            print(f"{self.player_name} takes -{damage} HP damage!")
            self.health -= damage
            print(f"{self.player_name} health {self.health} HP")
            return self.health

        else:
            return "That attack was very ineffective.."

    def attack(self, atk_amount):
        print(f"{self.player_name} Attacks!")
        return atk_amount

    def death(self):
        print(f"{self.player_name} has died..")

    def __str__(self):
        return self.player_name







