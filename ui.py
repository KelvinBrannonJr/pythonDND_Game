from player import Player
from enemy import Enemy
import random


class UI:
    def __init__(self):
        self.player_name = Player("Sir Kingston")
        self.enemy_name = Enemy("Green Slime")

    def six_sided_dice(self):
        if self.player_name.player_turn:
            roll_dice = input("Roll dice? Y/N \n").lower()
            if roll_dice == 'y':
                rand_roll = random.randint(1, 6)
                print(f"{self.player_name} rolled: {rand_roll}")
                return rand_roll
            else:
                print("You decided not to roll")

        elif self.enemy_name.enemy_turn:
            rand_roll = random.randint(1, 6)
            print(f"{self.enemy_name} rolled: {rand_roll}")

    def random_encounter_turn(self):
        random_generate_encounter = random.randint(1, 4)
        if random_generate_encounter == self.player_name.player_queue_number:
            print("Player's Turn")
            self.player_name.player_turn = True

        elif random_generate_encounter == self.enemy_name.enemy_queue_number:
            print("Enemy's Turn")
            self.enemy_name.enemy_turn = True

    def display_ui(self):
        print(" " * 35)
        print("****** DICE AND DUNGEONS ******")
        print("=" * 35)
        self.random_encounter_turn()
        if self.player_name.player_turn:
            user_command = input("Select a move: [ Atk, Flee ] \n").title()
            print("=" * 35)
            match user_command:
                case "Atk":
                    print(f"{self.player_name.name} Attacks!")

                case "Flee":
                    print(f"Like a coward {self.player_name.name}, fled crying!")

        elif self.enemy_name.enemy_turn:
            print("Enemy has taken the initiative!!")

        else:
            print("Travel time with no encounters")
