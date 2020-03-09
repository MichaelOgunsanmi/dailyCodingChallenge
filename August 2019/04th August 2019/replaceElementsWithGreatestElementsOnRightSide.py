# Source: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

# Level: Easy
#
# Date: 04th August 2019


"""Given an array arr, replace every element in that array with the greatest element among the elements to its right,
and replace the last element with -1.

After doing so, return the array.



Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]


Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
"""

# Solution
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxElement = arr[len(arr) - 1]
        arr[len(arr) - 1] = -1
        index = len(arr) - 2

        while index >= 0:
            val = arr[index]
            arr[index] = maxElement
            if val > maxElement:
                maxElement = val
            index -= 1

        return arr
