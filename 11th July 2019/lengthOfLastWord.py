# Source: https://leetcode.com/problems/length-of-last-word/

# Level: Easy

# Date: 11th July, 2019

# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last
# word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# Example:
#
# Input: "Hello World"
# Output: 5


class Solution:
    def lengthOfLastWord(self, s: str) -> int:  
        s = s.rstrip()
        if len(s) == 0:
            return 0

        length = 0
        pointer = len(s) - 1

        while s[pointer] != " " and pointer != -1:
            length += 1
            pointer -= 1

        return length
