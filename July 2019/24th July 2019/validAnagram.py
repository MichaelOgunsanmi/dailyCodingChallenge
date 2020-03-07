# Source: https://leetcode.com/problems/valid-anagram/

# Level: Easy

# Date: 24th July 2019

# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


class Solution:
    def isAnagram(self, stringInput: str, testInput: str) -> bool:
        if len(stringInput) != len(testInput):
            return False

        hashMap = {}

        for letter in stringInput:
            hashMap[letter] = hashMap.get(letter, 0) + 1

        for letter in testInput:
            if letter not in hashMap:
                return False
            hashMap[letter] -= 1

        for value in hashMap.values():
            if value != 0:
                return False
        return True
