"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/821/

Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""
import unittest
from collections import Counter


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        sign = ""
        if (numerator < 0 and denominator > 0
                or numerator > 0 and denominator < 0):
            sign = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        int_part = sign + str(numerator // denominator)
        numerator = numerator % denominator
        result = []
        c = Counter()
        periodical = False
        while numerator > 0:
            c[numerator] += 1
            if c.most_common(1)[0][1] == 3:
                periodical = True
                break
            if numerator < denominator:
                numerator *= 10
                result.append(numerator // denominator)
                numerator = numerator % denominator

        result = [str(x) for x in result]
        if not result:
            return int_part
        else:
            int_part = list(int_part)
            if periodical:
                n = sum((1 for x in c.most_common() if x[1] >= 2))
                int_part.append(".")
                int_part.extend(result[:-2 * n])
                int_part.append("(")
                int_part.extend(result[-2 * n:-n])
                int_part.append(")")
            else:
                int_part.append(".")
                int_part.extend(result)
            return "".join(int_part)


class TestSolution(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(s.fractionToDecimal(1, 6), "0.1(6)")
        self.assertEqual(s.fractionToDecimal(7, -12), "-0.58(3)")


if __name__ == "__main__":
    unittest.main()