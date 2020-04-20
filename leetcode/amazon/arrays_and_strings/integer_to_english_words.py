"""
https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/481/

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""
from collections import deque


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def foo(n):
            a = [
                "",
                "One",
                "Two",
                "Three",
                "Four",
                "Five",
                "Six",
                "Seven",
                "Eight",
                "Nine",
                "Ten",
                "Eleven",
                "Twelve",
                "Thirteen",
                "Fourteen",
                "Fifteen",
                "Sixteen",
                "Seventeen",
                "Eighteen",
                "Nineteen",
            ]
            b = [
                "",
                "Ten",
                "Twenty",
                "Thirty",
                "Forty",
                "Fifty",
                "Sixty",
                "Seventy",
                "Eighty",
                "Ninety",
            ]
            result = ""
            if n >= 100:
                result = f"{a[n//100]} Hundred "
            n = n % 100
            if n < 20:
                result += a[n]
            else:
                result += f"{b[n//10]} {a[n%10]}"
            return result.strip()

        c = [
            "",
            "Thousand",
            "Million",
            "Billion",
            "Trillion",
        ]

        i = 0
        x = deque()
        while num:
            y = num % 1000
            if y:
                if i > 0:
                    x.appendleft(c[i])
                x.appendleft(foo(y))
            num = num//1000
            i += 1
        return " ".join(x).strip()
