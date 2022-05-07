import random

from framework.card import Card, Suit, COLORED_SUITS
from framework.deck import Deck
from framework.player import Player


class Simpleton(Player):
    def play(self, deck: Deck) -> Card:
        val = None
        for card in self.hand:
            if deck.is_playable(card):
                if deck.play_card(card):
                    self.hand.remove(card)
                    val = card
                    break
        if not val:
            val = self.draw_and_play_if_possible(deck)
        return val

    def choose_suit(self, deck) -> Suit:
        return random.choice(COLORED_SUITS)
