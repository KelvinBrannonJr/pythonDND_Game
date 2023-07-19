import random


class Dice:
    def __int__(self, side, sides):
        self.side = 1
        self.sides = 6

    def roll_dice(self):
        rand_roll = random.randint(self.side, self.sides)
        print(f"You rolled: {rand_roll}")
        return rand_roll

    def ask_to_roll(self):
        ask_user_to_roll = input("Would you like to roll? Y/N \n").lower()
        if ask_user_to_roll == 'y':
            return self.roll_dice()
        if ask_user_to_roll == 'n':
            return print("You passed your turn to roll..")
