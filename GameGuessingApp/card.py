import random


class Suit:
    suit = {
        "Heart": 4,
        "Diamond": 3,
        "Club": 2,
        "Spade": 1,
        "Black Joker": 5,
        "Red Joker": 6,
    }


class Rank:
    rank = {
        "A": 14,
        "2": 15,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
    }


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __lt__(self, other):
        if Rank.rank[self.rank] == Rank.rank[other.rank]:
            return Suit.suit[self.suit] < Suit.suit[other.suit]
        return Rank.rank[self.rank] < Rank.rank[other.rank]

    def __gt__(self, other):
        if Rank.rank[self.rank] == Rank.rank[other.rank]:
            return Suit.suit[self.suit] > Suit.suit[other.suit]
        return Rank.rank[self.rank] > Rank.rank[other.rank]

    def __eq__(self, other):
        return (
            Rank.rank[self.rank] == Rank.rank[other.rank]
            and Suit.suit[self.suit] == Suit.suit[other.suit]
        )


class Deck:
    def __init__(self):
        self.cards = [
            Card(suit, rank)
            for suit in Suit.suit.keys()
            if suit not in ("Black Joker", "Red Joker")
            for rank in Rank.rank.keys()
        ] + [Card("Black Joker", "A"), Card("Red Joker", "A")]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()
