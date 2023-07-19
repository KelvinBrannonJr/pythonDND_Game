from ui import UI
from game import Game

if __name__ == "__main__":
    game = Game()
    hud = UI()
    while game.game_is_looping:
        hud.display_ui()

        print("Game Over")
        game.game_is_looping = False
