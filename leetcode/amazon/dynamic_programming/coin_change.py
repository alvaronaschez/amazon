"""
https://leetcode.com/explore/interview/card/amazon/80/dynamic-programming/2998/

Coin Change

You are given coins of different denominations and a total amount of money
amount. Write a function to compute the fewest number of coins that you need
to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""
from typing import List
from math import inf


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        c = [inf]*(amount+1)
        c[0] = 0
        for coin in coins:
            for a in range(coin, amount+1):
                c[a] = min(1+c[a-coin], c[a])
        return -1 if c[-1] == inf else c[-1]
