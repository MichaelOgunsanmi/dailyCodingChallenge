'''
Source: https://leetcode.com/problems/first-unique-character-in-a-string/

Level: Easy

Date: 06th July 2019

'''

'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''

class Solution:
    def firstUniqChar(self, string):
        hashTable = {}

        for index, elem in enumerate(string):
            if elem not in hashTable:
                hashTable[elem] = []
            hashTable[elem].append(index)

        minIndex = len(string)
        for value in hashTable.values():
            if len(value) == 1 and value[0] < minIndex:
                minIndex = value[0]
        if minIndex == len(string):
            return -1
        else:
            return minIndex