# Source: https://leetcode.com/problems/path-sum/
#
# Level: Easy
#
# Date: 03rd August 2019


"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""


# Solution

class Solution:
    def titleToNumber(self, stringInput: str) -> int:
        output = 0
        i = len(stringInput) - 1
        j = 0
        while i >= 0:
            output += pow(26, j) * (ord(stringInput[i]) - 64)
            i -= 1
            j += 1

        return output
