# Source: https://leetcode.com/problems/power-of-four/
# Level: Easy
#
# Date: 02nd August 2019


"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
"""


# Solution

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False

        while num % 4 == 0:
            num /= 4

        return num == 1
