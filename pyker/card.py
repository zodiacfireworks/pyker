from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .constants import VALUES

__all__ = ["Suit", "Value"]


class Suit(Enum):
    Spades = "S"
    S = "S"
    Hearts = "H"
    H = "H"
    Diamonds = "D"
    D = "D"
    Clubs = "C"
    C = "C"


class Value(Enum):
    Two = "2"
    Three = "3"
    Four = "4"
    Five = "5"
    Six = "6"
    Seven = "7"
    Eight = "8"
    Nine = "9"
    Ten = "T"
    Jack = "J"
    Queen = "Q"
    King = "K"
    Ace = "A"

    def __gt__(self, other: Value) -> bool:
        return VALUES.find(self.value) > VALUES.find(other.value)

    def __ge__(self, other: Value) -> bool:
        return VALUES.find(self.value) >= VALUES.find(other.value)


@dataclass
class Card:
    value: Value
    suit: Suit

    def __init__(self, str_value: str) -> None:
        if len(str_value) != 2:
            raise ValueError("Argument `srt_value` must have exactly 2 characters")

        value, suit = list(str_value.upper())
        self.value = Value(value)
        self.suit = Suit(suit)

    def __str__(self) -> str:
        return f"{self.value.value}{self.suit.value}"
