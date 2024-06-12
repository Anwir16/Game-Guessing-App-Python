import logging
from card import Deck
from player import Player, House

logging.basicConfig(level=logging.INFO)

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.house = House()
        self.current_reward = 0

    def play_round(self):
        if self.player.points < 25:
            logging.info("Player does not have enough points to continue.")
            return

        self.player.update_points(-25)
        self.house.receive_card(self.deck.deal())
        logging.info(f"House card: {self.house.card}")

        self.player.card = self.deck.deal()
        logging.info(f"Player card: {self.player.card}")

        guess = input("Guess if your card is greater or less than the house's card (greater/less): ").strip().lower()
        if self.player.make_guess(self.house.card, guess):
            self.current_reward += 20
            logging.info(f"Correct guess! Current reward: {self.current_reward} points.")
        else:
            self.current_reward = 0
            logging.info("Wrong guess. You lose the current round's reward.")

        if self.player.points >= 1000:
            logging.info("Congratulations! You win the game.")
        elif self.player.points < 30:
            logging.info("You do not have enough points. Game over.")

    def start_game(self):
        while self.player.points >= 30 and self.player.points < 1000:
            self.play_round()
            continue_game = input("Do you want to continue to the next round? (yes/no): ").strip().lower()
            if continue_game not in ("yes", "y"):
                self.player.update_points(self.current_reward)
                self.current_reward = 0
                logging.info(f"Player's total points: {self.player.points}")
                break
