from framework.deck import Deck


class Uno:
    def __init__(self):
        self.deck = Deck()

    def play(self):
        hand = self.deck.draw(7)
        print(hand)
        hand.sort()
        print(hand)


if __name__ == "__main__":
    uno = Uno()
    uno.play()