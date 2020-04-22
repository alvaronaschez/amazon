"""
https://leetcode.com/explore/interview/card/amazon/80/dynamic-programming/489/

Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

"""


def is_palindrome(s: str) -> bool:
    return s[::-1][:len(s)//2] == s[:len(s)//2]


def is_palindrome_old(s: str, i: int, j: int) -> bool:
    return s[i:j] == s[i:j][::-1]


def longestPalindrome(s: str) -> str:
    """
    iterate over all possible lengths
    then over all possible substring of that length
    there are 1+2+...+n-1 possibilities, so its O(n**2)
    """
    for n in reversed(range(len(s)+1)):
        for i in range(len(s)-n+1):
            if is_palindrome(s[i: i+n]):
                return s[i: i+n]


def longestPalindrome_bruteforce(s: str) -> str:
    """
    brute force:
    test all possible starts and ends
    """
    n = 0
    x = 0
    y = 0
    for i in range(len(s)+1):
        for j in range(i+1, len(s)+1):
            if j-i <= n:
                continue
            if is_palindrome_old(s, i, j):
                if j-i > n:  # redundant but cheap
                    x, y = i, j
                    n = j-i
    return s[x: y]


def longestPalindrome_dynamicprogramming(s: str) -> str:
    """dynamic programming"""
    a = [[False]*len(s) for _ in range(len(s))]
    m, x, y = 0, 0, -1
    for i in reversed(range(len(s))):
        for j in range(i-1, len(s)):
            a[i][j] = j-i+1 <= 1 or (j-i-1 <= 1 or a[i+1]
                                     [j-1]) and s[i] == s[j]
            if a[i][j] and j-i+1 >= m:
                m, x, y = j-i+1, i, j
    return s[x:y+1]
