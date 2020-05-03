"""
https://leetcode.com/explore/interview/card/amazon/84/recursion/521/

Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible
letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given
below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in
any order you want.
"""
import unittest
from typing import List
from itertools import product
"""
a = "".join([chr(i) for i in range(ord("a"), ord("z")+1)])
letters = [None, None]
for i in range(0, 8):
    start = i*3 if i+2 < 8 else i*3+1
    stop = start + 3 if i+2 not in (7, 9) else start + 4
    letters.append(a[start: stop])
"""
letters = [
    None,
    None,
    "abc",
    "def",
    "ghi",
    "jkl",
    "mno",
    "pqrs",
    "tuv",
    "wxyz",
]


def letter_combinations(digits: str) -> List[str]:
    if not digits:
        return []
    else:
        aux1 = letters[int(digits[-1])]
        aux2 = letter_combinations(digits[:-1])
        return [x + y for x in aux2 for y in aux1] or list(aux1)


def letter_combinations_2(digits: str) -> List[str]:
    """improvement"""
    a = (letters[int(d)] for d in digits)
    return ["".join(x) for x in product(*a) if x]


class TestLetterCombinations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inpt = "23"
        cls.output = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    def test_letter_combinations(self):
        self.assertCountEqual(letter_combinations(self.inpt), self.output)

    def test_letter_combinations_2(self):
        self.assertCountEqual(letter_combinations_2(self.inpt), self.output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
