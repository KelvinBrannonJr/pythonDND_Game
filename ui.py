from player import Player
from enemy import Enemy
from game import Game
import random


class UI:

    def __init__(self):
        self.game = Game()
        self.player = Player("Sir Kingston")
        self.enemy = Enemy("Green Slime")

    def six_sided_dice(self):
        if self.player.player_name.player_turn:
            roll_dice = input("Roll dice? Y/N \n").lower()
            if roll_dice == 'y':
                random_roll = random.randint(1, 6)
                print(f"{self.player.player_name} rolled: {random_roll}")
                return random_roll
            else:
                print("You decided not to roll")

        elif self.enemy.enemy_name.enemy_turn:
            rand_roll = random.randint(1, 6)
            print(f"{self.enemy.enemy_name} rolled: {rand_roll}")

    def random_encounter_turn(self):
        random_generate_encounter = random.randint(1, 4)
        if random_generate_encounter == self.player.player_queue_number:
            print(f"{self.enemy.enemy_name} Enemy Encountered!!!")
            print(f"{self.player.player_name}'s Turn")
            self.player.player_turn = True

        elif random_generate_encounter == self.enemy.enemy_queue_number:
            print(f"{self.enemy.enemy_name} Enemy Encountered!!!")
            self.enemy.enemy_turn = True

    def calculate_player_atk_to_enemy_damage(self, atk_damage):
        if atk_damage >= self.enemy.enemy_health:
            self.enemy.enemy_death()
            return self.random_encounter_turn()

        else:
            return self.enemy.enemy_take_damage(atk_damage)

    def calculate_enemy_atk_to_player_damage(self, enemy_atk_damage):
        if enemy_atk_damage >= self.player.health:
            self.player.death()
            return self.game.game_over()

        else:
            return self.player.takes_damage(enemy_atk_damage)

    def display_ui(self):
        while self.player.health >= 1:
            print(" " * 35)
            print("****** DICE AND DUNGEONS ******")
            print("=" * 35)
            self.random_encounter_turn()
            if self.player.player_turn:
                user_command = input("Select a move: [ Atk, Flee ] \n").title()
                print("=" * 35)
                match user_command:
                    case "Atk":
                        random_atk_dmg = random.randint(1, self.enemy.enemy_health)
                        if random_atk_dmg == self.enemy.enemy_health:
                            print("Critical Hit!!!")
                        final_player_atk_dmg = self.player.attack(random_atk_dmg)
                        self.calculate_player_atk_to_enemy_damage(final_player_atk_dmg)

                    case "Flee":
                        print(f"Like a coward {self.player.player_name}, fled crying!")
                        break

            elif self.enemy.enemy_turn:
                print(f"{self.enemy.enemy_name} Enemy has taken the initiative!!")
                random_atk_dmg = random.randint(1, self.player.health)
                final_enemy_atk_dmg = self.enemy.enemy_attack(random_atk_dmg)
                self.calculate_enemy_atk_to_player_damage(final_enemy_atk_dmg)

            else:
                print("Travel time with no encounters")

