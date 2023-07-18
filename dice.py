import random


class Dice:
    def __int__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        min_side = 1
        max_sides = 6
        rand_roll = random.randint(min_side, max_sides)
        print(f"You rolled: {rand_roll}")
        return rand_roll

    def ask_to_roll(self):
        ask_user_to_roll = input("Would you like to roll? Y/N \n").lower()
        if ask_user_to_roll == 'y':
            return self.roll_dice()
        if ask_user_to_roll == 'n':
            return print("You passed your turn to roll..")
