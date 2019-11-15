# Source: https://leetcode.com/problems/maximum-product-of-three-numbers/

# Level: Easy

# Date: 12th July, 2019

# Given an integer array, find three numbers whose product is maximum and output the maximum product.
#
# Example 1:
#
# Input: [1,2,3]
# Output: 6
#
#
# Example 2:
#
# Input: [1,2,3,4]
# Output: 24
#
#
# Note:
#
# The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        firstLargest = float('-inf')
        secondLargest = firstLargest
        thirdLargest = secondLargest
        firstSmallest = float('inf')
        secondSmallest = firstSmallest

        for num in nums:
            if num <= secondSmallest:
                firstSmallest = secondSmallest
                secondSmallest = num
            elif num <= firstSmallest:
                firstSmallest = num

            if num >= firstLargest:
                thirdLargest = secondLargest
                secondLargest = firstLargest
                firstLargest = num
            elif num >= secondLargest:
                thirdLargest = secondLargest
                secondLargest = num
            elif num >= thirdLargest:
                thirdLargest = num

        maximumProd1 = firstLargest * secondLargest * thirdLargest
        maximumProd2 = firstSmallest * secondSmallest * firstLargest

        return max(maximumProd1, maximumProd2)