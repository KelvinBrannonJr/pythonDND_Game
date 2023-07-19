from player import Player
from enemy import Enemy


class UI:
    def __init__(self):
        self.sir_kingston = Player("Sir Kingston")
        self.slime = Enemy("Green Slime")

    def display_ui(self):
        print("=" * 35)
        user_command = input("Select a move: [ Atk, Flee ] \n").title()
        print("=" * 35)
        match user_command:
            case "Atk":
                print(f"{self.sir_kingston.name} Attacks!")

            case "Flee":
                print(f"Like a coward {self.sir_kingston.name}, fled crying!")


