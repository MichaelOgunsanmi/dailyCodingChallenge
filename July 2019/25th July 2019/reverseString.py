# Source: https://leetcode.com/problems/reverse-string/

# Level: Easy

# Date: 25th July 2019, 2019

# Write a function that reverses a string. The input string is given as an array of characters char[].
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1)
# extra memory.
#
# You may assume all the characters consist of printable ascii characters.
#
#
#
# Example 1:
#
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
#
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # method 1
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

        # method 2
        index = 0
        while index < int(len(s) / 2):
            s[index], s[len(s) - 1 - index] = s[len(s) - 1 - index], s[index]
            index += 1

        # method 3
        s.reverse()

        # method 4
        if len(s) > 0:
            self.helper(0, s)

    def helper(self, index, s):
        if index < int(len(s) / 2) - 1:
            self.helper(index + 1, s)

        s[index], s[len(s) - 1 - index] = s[len(s) - 1 - index], s[index]
