# Source: https://leetcode.com/problems/partition-labels/
#
# Date: 19th August 2019

"""
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that
each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
"""


# Solution
from typing import List


class Solution:
    def partitionLabels(self, stringInput: str) -> List[int]:
        rightmostIndex = {c: i for i, c in enumerate(stringInput)}
        leftIndex, rightIndex = 0, 0

        output = []
        for index, letter in enumerate(stringInput):

            rightIndex = max(rightIndex, rightmostIndex[letter])

            if index == rightIndex:
                output += [rightIndex - leftIndex + 1]
                leftIndex = index + 1

        return output
