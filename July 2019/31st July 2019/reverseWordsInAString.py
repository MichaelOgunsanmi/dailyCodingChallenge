# Source: https://leetcode.com/problems/reverse-words-in-a-string/
#
# Level: Medium
#
# Date: 31st July 2019


"""
Given an input string, reverse the string word by word.



Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Note:

A word is defined as a sequence of non-space characters. Input string may contain leading or trailing spaces.
However, your reversed string should not contain leading or trailing spaces. You need to reduce multiple spaces
between two words to a single space in the reversed string.


Follow up:

For C programmers, try to solve it in-place in O(1) extra space.
"""


# Solution


class Solution:
    def reverseWords(self, stringInput: str) -> str:
        stringInput = stringInput.strip().split(' ')
        stringInput = stringInput[::-1]
        i = 0

        while i < len(stringInput):
            prev = i
            if stringInput[i] == '':
                while i < len(stringInput) and stringInput[i] == '':
                    i += 1
                stringInput = stringInput[:prev] + stringInput[i:]
                i = prev

            i += 1
        return ' '.join(stringInput)
