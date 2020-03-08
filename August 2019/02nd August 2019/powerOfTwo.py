# Source: https://leetcode.com/problems/power-of-two/
#
# Level: Easy
#
# Date: 02nd August 2019


"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
"""


# Solution

class Solution:
    def isPowerOfTwo(self, num: int) -> bool:
        if num < 1:
            return False

        while num % 2 == 0:
            num /= 2

        return num == 1
