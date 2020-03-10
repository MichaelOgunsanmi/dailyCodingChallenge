# Source: https://leetcode.com/problems/longest-common-prefix/

# Level: Easy
#
# Date: 06th August 2019


"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


# Solution
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]

        index = 0

        while index <= len(strs) - 2:
            if len(prefix) == 0:
                return ""

            newWord = strs[index + 1]

            count = 0

            while count < len(prefix) and count < len(newWord):
                if prefix[count] == newWord[count]:
                    count += 1
                    continue
                break

            prefix = prefix[:count]
            index += 1

        return prefix
