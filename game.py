"""
OBJECTIVE
- Set up the gameplay rules
- Provide game loop in main.py
- Create Game UI for player via terminal
- Create randomize encounters with enemies
- Success of player decisions on outcome of dice roll
- Allow player to exit program
"""


class Game:
    def __init__(self):
        self.game_is_looping = True
        self.is_dead = False

    def game_over(self):
        print("Game Over")
        self.game_is_looping = False
