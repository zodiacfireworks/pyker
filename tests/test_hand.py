import unittest

import pytest

from pyker import PokerHand, Result, Suit, Value, __version__


class PokerHandTest(unittest.TestCase):
    version = __version__

    @staticmethod
    def test_poker_hand_constructor():
        hand = PokerHand("AS 2S 3S 5S 4S")
        assert hand.values == [
            Value.Ace,
            Value.Two,
            Value.Three,
            Value.Five,
            Value.Four,
        ]
        assert hand.suits == [
            Suit.Spades,
            Suit.Spades,
            Suit.Spades,
            Suit.Spades,
            Suit.Spades,
        ]

    @staticmethod
    def test_poker_hand_allow_repeat():
        with pytest.raises(ValueError) as excinfo:
            PokerHand("AS AS 3S 5S 4S", allow_repeat=False)

        assert (
            "Argument `str_cards` must have exactly 5 string "
            "representations of cards"
        ) in str(excinfo.value)

    @staticmethod
    def test_proker_hand_str():
        assert str(PokerHand("AS 2S 3S 5S 4S")) == "2S 3S 4S 5S AS"

    @staticmethod
    def test_poker_hand_full_sstraigh():
        assert PokerHand("AS 2S 3S 5S 4S").score[0] == (5,)

    @staticmethod
    def test_poker_hand_comparsion():
        assert (
            PokerHand("TC TH 5C 5H KH").compare_with(PokerHand("9C 9H 5C 5H AC"))
            == Result.WIN
        )
        assert (
            PokerHand("TS TD KC JC 7C").compare_with(PokerHand("JS JC AS KC TD"))
            == Result.LOSS
        )
        assert (
            PokerHand("7H 7C QC JS TS").compare_with(PokerHand("7D 7C JS TS 6D"))
            == Result.WIN
        )
        assert (
            PokerHand("5S 5D 8C 7S 6H").compare_with(PokerHand("7D 7S 5S 5D JS"))
            == Result.LOSS
        )
        assert (
            PokerHand("AS AD KD 7C 3D").compare_with(PokerHand("AD AH KD 7C 4S"))
            == Result.LOSS
        )
        assert (
            PokerHand("TS JS QS KS AS").compare_with(PokerHand("AC AH AS AS KS"))
            == Result.WIN
        )
        assert (
            PokerHand("TS JS QS KS AS").compare_with(PokerHand("TC JS QC KS AC"))
            == Result.WIN
        )
        assert (
            PokerHand("TS JS QS KS AS").compare_with(PokerHand("QH QS QC AS 8H"))
            == Result.WIN
        )
        assert (
            PokerHand("AC AH AS AS KS").compare_with(PokerHand("TC JS QC KS AC"))
            == Result.WIN
        )
        assert (
            PokerHand("AC AH AS AS KS").compare_with(PokerHand("QH QS QC AS 8H"))
            == Result.WIN
        )
        assert (
            PokerHand("TC JS QC KS AC").compare_with(PokerHand("QH QS QC AS 8H"))
            == Result.WIN
        )
        assert (
            PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JH JC JS JD TH"))
            == Result.WIN
        )
        assert (
            PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("4H 5H 9H TH JH"))
            == Result.WIN
        )
        assert (
            PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("7C 8S 9H TH JH"))
            == Result.WIN
        )
        assert (
            PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("TS TH TD JH JD"))
            == Result.WIN
        )
        assert (
            PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C"))
            == Result.WIN
        )
        assert (
            PokerHand("JH JC JS JD TH").compare_with(PokerHand("4H 5H 9H TH JH"))
            == Result.WIN
        )
        assert (
            PokerHand("JH JC JS JD TH").compare_with(PokerHand("7C 8S 9H TH JH"))
            == Result.WIN
        )
        assert (
            PokerHand("JH JC JS JD TH").compare_with(PokerHand("TS TH TD JH JD"))
            == Result.WIN
        )
        assert (
            PokerHand("JH JC JS JD TH").compare_with(PokerHand("JH JD TH TC 4C"))
            == Result.WIN
        )
        assert (
            PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("7C 8S 9H TH JH"))
            == Result.WIN
        )
        assert (
            PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("TS TH TD JH JD"))
            == Result.LOSS
        )
        assert (
            PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C"))
            == Result.WIN
        )
        assert (
            PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("TS TH TD JH JD"))
            == Result.LOSS
        )
        assert (
            PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C"))
            == Result.WIN
        )
        assert (
            PokerHand("TS TH TD JH JD").compare_with(PokerHand("JH JD TH TC 4C"))
            == Result.WIN
        )


if __name__ == "__main__":
    unittest.main()
