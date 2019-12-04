# Source: https://leetcode.com/problems/product-of-array-except-self/

# Level: Medium

# Date: 18th July, 2019


# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product
# of all the elements of nums except nums[i].
#
# Example:
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Note: Please solve it without division and in O(n).
#
# Follow up: Could you solve it with constant space complexity? (The output array does not count as extra space for
# the purpose of space complexity analysis.)
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalMultiplication = 1
        change = False
        hasZero = False
        allZeros = False

        for num in nums:
            if num == 0:
                if hasZero is True:
                    allZeros = True
                hasZero = True
                continue
            totalMultiplication *= num
            change = True

        output = []
        if change is False:
            totalMultiplication = 0

        for num in nums:
            if allZeros is True:
                output.append(0)
                continue
            if hasZero is True:
                if num != 0:
                    output.append(0)
                else:
                    output.append(totalMultiplication)
                continue
            output.append(int(totalMultiplication * (num ** -1)))

        return output
