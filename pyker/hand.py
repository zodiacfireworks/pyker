from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List

from .card import Card, Suit, Value
from .constants import VALUES

__all__ = ["Result", "PokerHand"]


class Result(Enum):
    WIN = True
    LOSS = False


@dataclass
class PokerHand:
    cards: List[Card]
    allow_repeat: bool

    def __init__(self, str_cards, allow_repeat=True):
        cards = str_cards.split(" ")

        if not allow_repeat:
            cards = set(cards)

        if len(cards) != 5:
            raise ValueError(
                "Argument `str_cards` must have exactly 5 string "
                "representations of cards"
            )

        self.allow_repeat = allow_repeat
        self.cards = [Card(card) for card in cards]

    def __str__(self) -> str:
        return " ".join(self.as_string_list())

    def __eq__(self, other: object) -> bool:
        as_string_list = getattr(other, "as_string_list")
        if callable(as_string_list):
            return sorted(self.as_string_list()) == sorted(as_string_list())

        return False

    def __gt__(self, other: PokerHand):
        """Determine with hand is major than other.

        The comparsion is made in function of the score of each hand.

        """
        scores = [(self, self.score), (other, other.score)]
        winner = sorted(scores, key=lambda x: x[1])[-1][0]
        return winner == self

    def as_string_list(self):
        return sorted([str(card) for card in self.cards])

    def compare_with(self, other: PokerHand):
        return Result(self > other)

    @property
    def values(self) -> List[Value]:
        return [card.value for card in self.cards]

    @property
    def suits(self) -> List[Suit]:
        return [card.suit for card in self.cards]

    @property
    def histogram(self):
        hand_values = self.values
        histogram = [(hand_values.count(value), value) for value in set(hand_values)]
        freq, values = zip(*sorted(histogram, reverse=True))
        return freq, values

    @property
    def score(self) -> tuple:
        """Return the score of a poker hand.

        This was implemented acording to this reference
        http://nsayer.blogspot.com/2007/07/algorithm-for-evaluating-poker-hands.html

        """
        score, values = self.histogram
        hand_suits = self.suits
        # Handle case if we have 5 cards with distinct values
        if len(values) == 5:
            straight = VALUES.find(values[0].value) - VALUES.find(values[4].value) == 4
            flush = len(set(hand_suits)) == 1

            # Adjust if 5 high straight. If so, the use Ace as one
            if values[0:2] == (Value.Ace, Value.Five):
                values = (Value.Five, Value.Four, Value.Three, Value.Two, Value.Ace)
                straight = True

            # Predefined sore frecuencies to assign if we have no pair, straight,
            # flush, or straight flush
            score = ([1, (3, 1, 1, 1)], [(3, 1, 1, 2), (5,)])[flush][straight]
        return score, values
