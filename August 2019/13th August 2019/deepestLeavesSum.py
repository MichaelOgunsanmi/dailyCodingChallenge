# Source: https://leetcode.com/problems/deepest-leaves-sum/
#
# Date: 13th August 2019


"""
Given a binary tree, return the sum of values of its deepest leaves.


Example 1:



Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15


Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
"""


# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deepestLeavesSum(self, rootNode: TreeNode) -> int:
        totalSum = [0]
        getLeaves(rootNode, totalSum, 0, [0])

        return totalSum[0]


def getLeaves(currentNode, totalSum, depth, maxDepth):
    if isLeaf(currentNode):
        if depth == maxDepth[0]:
            totalSum[0] += currentNode.val
        elif depth > maxDepth[0]:
            totalSum[0] = currentNode.val
            maxDepth[0] = depth
        else:
            return
        return

    if currentNode.left is not None:
        getLeaves(currentNode.left, totalSum, depth + 1, maxDepth)

    if currentNode.right is not None:
        getLeaves(currentNode.right, totalSum, depth + 1, maxDepth)


def isLeaf(currentNode):
    return currentNode.left is None and currentNode.right is None
