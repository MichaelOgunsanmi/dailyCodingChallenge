# Source: https://leetcode.com/problems/implement-strstr/

# Level: Easy
#
# Date: 06th August 2019


"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr()
and Java's indexOf(). """


# Solution


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (len(needle) == 0 and len(haystack) == 0) or len(needle) == 0:
            return 0

        index = 0

        while index <= len(haystack) - len(needle):
            if haystack[index] == needle[0] and haystack[index: index + len(needle)] == needle:
                return index
            index += 1

        return -1
