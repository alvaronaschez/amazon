"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/744/

Count Primes
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
from math import sqrt, ceil


class Solution:
    def countPrimes(self, n: int) -> int:
        """la criba de eratostenes"""
        if n < 2:
            return 0
        aux = [1]*n
        aux[:2] = 0, 0
        for i in range(2, ceil(sqrt(n))):
            if aux[i]:
                x = 2*i
                while x < n:
                    aux[x] = 0
                    x += i
        return sum(aux)
