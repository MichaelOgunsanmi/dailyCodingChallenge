# Source: https://leetcode.com/problems/valid-palindrome/submissions/

# Level: Easy

# Date: 15th July, 2019

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.
#
# Example 1:
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:
#
# Input: "race a car"
# Output: false

class Solution:
    def isPalindrome(self, inputString: str) -> bool:
        inputString = inputString.lower().strip()

        leftIndex = 0
        rightIndex = len(inputString) - 1

        while leftIndex <= rightIndex:
            if not inputString[leftIndex].isalnum():
                leftIndex += 1
                continue
            if not inputString[rightIndex].isalnum():
                rightIndex -= 1
                continue

            if inputString[leftIndex] != inputString[rightIndex]:
                return False

            leftIndex += 1
            rightIndex -= 1

        return True
