'''
Source: https://leetcode.com/problems/longest-palindrome/

Level: Easy

Date: 6th July, 2019

'''

'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''

class Solution:
    def longestPalindrome(self, stringInput):
        hashTable = {}
        for element in stringInput:
            hashTable[element] = hashTable.get(element, 0) + 1 
        
        output = 0
        possible = False
        for element in hashTable:
            value = hashTable[element]
            if value % 2 == 0:
                output += value
            else:
                output += (2*(value//2))
                possible = True 
        if possible:
            output += 1
            
        return output

        