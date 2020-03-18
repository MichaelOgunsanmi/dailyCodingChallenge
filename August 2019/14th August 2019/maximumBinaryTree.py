# Source: https://leetcode.com/problems/maximum-binary-tree/
#
# Date: 14th August 2019


"""
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
Note:
The size of the given array will be in the range [1,1000].
"""

# Solution


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        maxIndex = findMaxIndex(nums)

        rootNode = TreeNode(nums[maxIndex])
        leftSide = nums[:maxIndex]
        rightSide = nums[maxIndex + 1:]

        if len(leftSide) != 0:
            if len(leftSide) == 1:
                rootNode.left = TreeNode(leftSide[0])
            else:
                rootNode.left = self.constructMaximumBinaryTree(leftSide)

        if len(rightSide) != 0:
            if len(rightSide) == 1:
                rootNode.right = TreeNode(rightSide[0])
            else:
                rootNode.right = self.constructMaximumBinaryTree(rightSide)

        return rootNode


def findMaxIndex(arr):
    maxVal = float('-inf')
    maxIndex = -1
    for i in range(len(arr)):
        if arr[i] > maxVal:
            maxIndex = i
            maxVal = arr[i]

    return maxIndex
