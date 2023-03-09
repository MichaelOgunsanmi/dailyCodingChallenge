# Source: https://leetcode.com/problems/longest-palindromic-substring/
#
# Date: 21st August 2019


"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


# Solution


class Solution:
    def longestPalindrome(self, inputString: str) -> str:
        if inputString is None or len(inputString) == 0:
            return ""

        startIndex = 0
        endIndex = 0

        currentIndex = 0

        while currentIndex < len(inputString):
            possibleOddLengthPalindrome = distanceFromMiddle(inputString, currentIndex, currentIndex)
            possibleEvenLengthPalindrome = distanceFromMiddle(inputString, currentIndex, currentIndex + 1)

            currentPalindromeLength = max(possibleOddLengthPalindrome, possibleEvenLengthPalindrome)

            if currentPalindromeLength > endIndex - startIndex:
                startIndex = currentIndex - int((currentPalindromeLength - 1) / 2)
                endIndex = currentIndex + int(currentPalindromeLength / 2)

            currentIndex += 1

        return inputString[startIndex: endIndex + 1]


def distanceFromMiddle(inputString, leftIndex, rightIndex):
    if inputString is None or leftIndex > rightIndex:
        return 0

    while leftIndex >= 0 and rightIndex < len(inputString) and inputString[leftIndex] == inputString[rightIndex]:
        leftIndex -= 1
        rightIndex += 1

    return rightIndex - leftIndex - 1
