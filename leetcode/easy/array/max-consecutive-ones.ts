// https://leetcode.com/problems/max-consecutive-ones

/*
485. Max Consecutive Ones
Easy

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
*/

function findMaxConsecutiveOnesTs(nums: number[]): number {
    let m: number = 0
    let c: number = 0
    for (let num of nums) {
        if (num === 1) {
            c++
        } else {
            c = 0
        }
        m = Math.max(m, c)
    }
    return m
};
