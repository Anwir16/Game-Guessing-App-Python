# main.py

from game import Game
from player import Player

def main():
    game = Game()
    game.start_game()
    player = Player("Player")
    if player.points >= 1000:
        print("You Win")

if __name__ == "__main__":
    main()
