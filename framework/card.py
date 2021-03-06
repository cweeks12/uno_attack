from enum import Enum, auto
from functools import total_ordering


@total_ordering
class Suit(Enum):
    """
    Top level enum that holds all of the available suits
    """
    RED = auto()
    GREEN = auto()
    YELLOW = auto()
    BLUE = auto()
    WILD = auto()

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


@total_ordering
class Value(Enum):
    """
    Enumerated class that holds the values of the Uno cards
    """
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    SKIP = auto()
    DRAW_2 = auto()
    REVERSE = auto()
    WILD = auto()
    DRAW_4 = auto()

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


COLORED_SUITS = list(filter(lambda x: x != Suit.WILD, Suit))
COLORED_VALUES = list(filter(lambda x: x not in [Value.WILD, Value.DRAW_4], Value))
NUMERIC_VALUES = list(filter(lambda x: x not in [Value.SKIP, Value.REVERSE, Value.DRAW_2], COLORED_VALUES))


@total_ordering
class Card:
    def __init__(self, suit: Suit, value: Value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.suit.name.lower()} {self.value.name.lower()}"

    def __repr__(self):
        return f"{self.suit.name} {self.value.name}"

    def __lt__(self, other):
        return self.value < other.value if self.suit == other.suit else self.suit < other.suit

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit

    def is_playable(self, other):
        """
        This function returns a boolean value to indicate whether or not the other card is playable on this one.
        The order doesn't matter because it just needs to match one aspect, and they're commutative
        :param other: Another card to compare to.
        :return: True if the card is playable, False if not
        """
        return self.value == other.value or self.suit == other.suit or self.suit == Suit.WILD or other.suit == Suit.WILD
