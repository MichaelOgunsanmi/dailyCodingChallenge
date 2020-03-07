# Source: https://leetcode.com/problems/reverse-words-in-a-string-iii/

# Level: Easy

# Date: 21st July 2019, 2019

# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving
# whitespace and initial word order.
#
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.


class Solution:
    def reverseWords(self, stringInput: str) -> str:
        return " ".join([x[::-1] for x in stringInput.split()])
