"""
OBJECTIVE
- Add mechanic to allow enemy attacks to randomly miss.
"""


class Enemy:
    def __init__(self, enemy_name):
        self.enemy_name = enemy_name
        self.enemy_health = 100
        self.enemy_queue_number = 3
        self.enemy_turn = False

    def get_enemy_health(self):
        print(self.enemy_health)
        return self.enemy_health

    def enemy_take_damage(self, enemy_damage):
        if enemy_damage > 0:
            print(f"{self.enemy_name} takes -{enemy_damage} HP damage!")
            self.enemy_health -= enemy_damage
            print(f"{self.enemy_name} health {self.enemy_health} HP\n")
            return self.enemy_health

        else:
            return "That attack was very ineffective.."

    def enemy_attack(self, enemy_atk_amount):
        print(f"{self.enemy_name} Attacks!")
        return enemy_atk_amount

    def enemy_death(self):
        return print(f"{self.enemy_name} was defeated!")

    def __str__(self):
        return self.enemy_name
