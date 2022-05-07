from framework.card import Card, Suit
from framework.deck import Deck


class Player:
    def __init__(self):
        self.hand = []

    def draw(self, deck: Deck, number: int = 1) -> list[Card]:
        drawn_cards = deck.draw(number)
        self.hand += drawn_cards
        print(f"DREW: {drawn_cards}")
        return drawn_cards

    def draw_hand(self, deck: Deck) -> list[Card]:
        return self.draw(deck, 7)

    def play(self, deck: Deck) -> Card:
        """
        This is a method to use in your inherited class when defining a player. This must be overridden in your
        defined class
        :param deck: The current deck you're playing with
        :return: Boolean value if you were able to play or not
        """
        raise NotImplementedError("Inherit this class in your player class")

    def choose_suit(self, deck) -> Suit:
        raise NotImplementedError("Inherit this class in your player class")

    def draw_and_play_if_possible(self, deck: Deck) -> Card:
        drawn_card = self.draw(deck)[0]
        if deck.is_playable(drawn_card):
            deck.play_card(drawn_card)
            self.hand.remove(drawn_card)
            return drawn_card
        return None

    def hand_empty(self):
        return len(self.hand) == 0

    def __str__(self):
        return f"{self.__class__.__name__}: {len(self.hand)} cards"

