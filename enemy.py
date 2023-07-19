class Enemy:
    def __init__(self, enemy_name):
        self.enemy_name = enemy_name
        self.enemy_health = 100

    def get_enemy_health(self):
        return self.enemy_health

    def enemy_take_damage(self, enemy_dmg):
        print(f"{self.enemy_name} takes -{enemy_dmg} HP damage!")
        new_enemy_health = self.enemy_health - enemy_dmg
        print(f"{self.enemy_name} health {new_enemy_health} HP\n")
        self.__str__()
        return new_enemy_health

    def enemy_attack(self, enemy_atk_amount):
        print(f"{self.enemy_name} attacks!")
        self.__str__()
        return enemy_atk_amount

    def enemy_death(self):
        if self.enemy_health <= 0:
            print(f"{self.enemy_name} was defeated!")
        return

    def print(self):
        print(f"{self.enemy_name} Encountered!\n")
        self.__str__()
