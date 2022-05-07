from itertools import product
import random

from framework.card import Card, Suit, Value, COLORED_SUITS, COLORED_VALUES


class Deck:
    initial_deck = [Card(suit, value) for suit, value in product(COLORED_SUITS, COLORED_VALUES)] + \
                   [Card(suit, value) for suit, value in product(COLORED_SUITS, COLORED_VALUES) if value != Value.ZERO] \
                   + [Card(Suit.WILD, Value.WILD) for i in range(4)] + [Card(Suit.WILD, Value.DRAW_4) for i in range(4)]

    def __init__(self):
        self._draw_pile = self.initial_deck.copy()
        random.shuffle(self._draw_pile)

        # Start with an empty discard pile
        # Discard pile is listed from the bottom up, i.e. first card is index [0], top card is at [-1] to save
        # on computation time
        self.discard_pile = []

    def draw(self, number=1):
        # If you don't have enough cards to draw
        if len(self._draw_pile) < number:
            # Draw the rest of the cards
            cards = self._draw_pile.copy()
            # Move all but the top card of the discard pile into the draw pile
            self._draw_pile = self.discard_pile[:-1]
            self.discard_pile = self.discard_pile[-1:]
            # Shuffle
            random.shuffle(self._draw_pile)
            # Draw the rest of the cards off the top
            cards += self.draw(number - len(cards))
        else:
            cards = self._draw_pile[:number]
            self._draw_pile = self._draw_pile[number:]
        return cards

    def create_discard_pile(self):
        self.discard_pile = self.draw(1)

    def is_playable(self, card: Card):
        return card.is_playable(self.top_card)

    @property
    def top_card(self) -> Card:
        return self.discard_pile[-1]

    def play_card(self, card: Card):
        if card.is_playable(self.discard_pile[-1]):
            self.discard_pile.append(card)
            return True
        else:
            return False

