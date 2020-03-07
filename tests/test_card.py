import unittest

import pytest

from pyker import Card, Suit, Value, __version__


class CardTest(unittest.TestCase):
    version = __version__

    @staticmethod
    def test_card_constructor():
        card = Card("AS")
        assert card.value == Value.Ace
        assert card.suit == Suit.Spades

    @staticmethod
    def test_card_letter_restriction():
        with pytest.raises(ValueError) as excinfo:
            Card("FAS")

        assert "Argument `srt_value` must have exactly 2 characters" in str(
            excinfo.value
        )

    @staticmethod
    def test_card_comparsion():
        assert Card("TC") == Card("TC")
        assert Card("AS") == Card("AS")
        assert Card("JD") == Card("JD")


if __name__ == "__main__":
    unittest.main()
