import unittest

from .roads_and_libraries import roads_and_libraries


class TestRoadsAndLibraries(unittest.TestCase):
    def test_roads_and_libraries(self):
        data = (
            (
                (3, 2, 1,
                 [(1, 2), (3, 1), (2, 3)]
                 ),
                4
            ),
            (
                (6, 2, 5,
                 [(1, 3), (3, 4), (2, 4), (1, 2), (2, 3), (5, 6)]
                 ),
                12
            ),
        )
        for i, o in data:
            self.assertEqual(roads_and_libraries(*i), o)
