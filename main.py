import random

from framework.card import Card, Suit, Value, NUMERIC_VALUES
from framework.deck import Deck
from framework.player import Player
from players.simpleton import Simpleton


class Uno:
    def __init__(self):
        self.deck = Deck()
        self.players = None
        self.reverse = False
        self._current_player_idx = 0

    @property
    def current_player(self) -> Player:
        return self.players[self._current_player_idx]

    def setup(self) -> None:
        self.players = [Simpleton(), Simpleton()]
        for player in self.players:
            player.draw_hand(self.deck)

        self.deck.create_discard_pile()

        # Randomly select a first player
        self._current_player_idx = random.randint(0, len(self.players)-1)

    def play_turn(self, player: Player) -> Card:
        return player.play(self.deck)

    def enact_card(self, card: Card) -> None:
        # If card is None or its value is just a number it does nothing
        if not card or card.value in NUMERIC_VALUES:
            return
        # If it's a skip, advance play a step
        if card.value == Value.SKIP:
            self.advance_play()
            return
        # If it's a draw 2, advance to the next player and draw 2
        elif card.value == Value.DRAW_2:
            self.advance_play()
            self.current_player.draw(self.deck, 2)
            return
        # If it's a reverse, reverse the play order
        elif card.value == Value.REVERSE:
            self.reverse = not self.reverse
            return

        if card.suit == Suit.WILD:
            self.deck.top_card.suit = self.current_player.choose_suit(self.deck)
        if card.value == Value.DRAW_4:
            self.advance_play()
            self.current_player.draw(self.deck, 4)

    def advance_play(self):
        self._current_player_idx = self._current_player_idx - 1 if self.reverse else self._current_player_idx + 1
        if self._current_player_idx < 0:
            self._current_player_idx = len(self.players) - 1
        if self._current_player_idx == len(self.players):
            self._current_player_idx = 0

    def play(self):
        self.setup()
        try:
            while True:
                if self.deck.top_card.value == Value.WILD:
                    print(f"WILD CARD: {self.deck.top_card}")
                print(f"TOP CARD: {self.deck.top_card}")
                print(f"HAND: {len(self.current_player.hand)} {self.current_player.hand}")
                played_card = self.play_turn(self.current_player)
                print(f"PLAYED: {played_card}")
                print(f"HAND AFTER PLAYING: {len(self.current_player.hand)} {self.current_player.hand}")
                if self.current_player.hand_empty():
                    break
                self.enact_card(played_card)
                self.advance_play()
                print()
                print()
        except KeyboardInterrupt:
            return
        print(f"{self.current_player} #{self._current_player_idx} is the winner!")


if __name__ == "__main__":
    uno = Uno()
    uno.play()
