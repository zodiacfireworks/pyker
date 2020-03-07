import unittest

from pyker import Value, __version__


class ValueTest(unittest.TestCase):
    version = __version__

    @staticmethod
    def test_value_comparsion():
        assert Value("T") == Value("T")
        assert Value("A") > Value("5")
        assert Value("J") >= Value("J")
        assert Value("5") >= Value("2")
        assert Value("Q") <= Value("K")


if __name__ == "__main__":
    unittest.main()
