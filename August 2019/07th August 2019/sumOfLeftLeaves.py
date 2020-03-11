# Source: https://leetcode.com/problems/sum-of-left-leaves/

# Level: Easy
#
# Date: 07th August 2019


"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""


# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, rootNode: TreeNode) -> int:
        if rootNode is None:
            return 0

        totalSum = [0]
        findSum(rootNode, totalSum)
        return totalSum[0]


def findSum(currentNode, totalSum):
    if currentNode.left is not None:
        if not isLeaf(currentNode) and isLeaf(currentNode.left):
            totalSum[0] += currentNode.left.val
        findSum(currentNode.left, totalSum)

    if currentNode.right is not None:
        findSum(currentNode.right, totalSum)

    return


def isLeaf(currentNode):
    return currentNode.left is None and currentNode.right is None
