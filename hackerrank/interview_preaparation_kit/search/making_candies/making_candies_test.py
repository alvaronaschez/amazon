import unittest

from .making_candies import minimumPasses


class TestCandies(unittest.TestCase):
    def test_minimum_passes(self):
        data = (
            ((1, 1, 6, 45), 16),
            ((4, 5, 436, 410), 21),
            ((1, 1, 1000000000000, 1000000000000), 1000000000000),
            ((1, 1, 6, 45), 16),
        )
        for i, o in data:
            self.assertEqual(minimumPasses(*i), o)


if __name__ == '__main__':
    unittest.main()
