class Player:
    def __init__(self, name):
        self.name = name
        self.points = 60
        self.card = None

    def make_guess(self, house_card, guess):
        return (guess == "greater" and self.card > house_card) or (
            guess == "less" and self.card < house_card
        )

    def update_points(self, amount):
        self.points += amount


class House:
    def __init__(self):
        self.card = None

    def receive_card(self, card):
        self.card = card
