# Source: https://leetcode.com/problems/reverse-integer/submissions/

# Level: Easy

# Date: 14th July 2019, 2019


# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120 Output: 21 Note: Assume we are dealing with an environment which could only store integers within the
# 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0
# when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        while x % 10 == 0:
            x //= 10

        possible = int(str(abs(x))[::-1])
        if x < 0 :
            return -1 * possible if -1 * possible > -pow(2,31) - 1 else 0
        return possible if possible < pow(2,31) - 1 else 0
