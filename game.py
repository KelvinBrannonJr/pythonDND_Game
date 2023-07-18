import player
from player import Player
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
        is_dead = False
        self.health = Player.get_health(player.sir_kingston)

    def death(self):
        if self.health <= 0:
            is_dead = True
            return self.game_over()

    def game_over(self):
        return print("Game Over")
