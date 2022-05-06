from itertools import product
import random

from framework.card import Card, Suit, Value, NUMERIC_SUITS, NUMERIC_VALUES


class Deck:
    initial_deck = [Card(suit, value) for suit, value in product(NUMERIC_SUITS, NUMERIC_VALUES)] + \
                   [Card(suit, value) for suit, value in product(NUMERIC_SUITS, NUMERIC_VALUES) if value != Value.ZERO]\
                    + [Card(Suit.WILD, Value.WILD)] * 4 + [Card(Suit.WILD, Value.DRAW_4)] * 4

    def __init__(self):
        self.draw_pile = self.initial_deck.copy()
        random.shuffle(self.draw_pile)

        # Start with an empty discard pile
        self.discard_pile = []

    def draw(self, number=1):
        if len(self.draw_pile) < number:
            # Shuffle discard pile
            pass
        cards = self.draw_pile[0:number]
        self.draw_pile = self.draw_pile[number:]
        return cards

    def create_discard_pile(self):
        self.discard_pile = self.draw(1)

