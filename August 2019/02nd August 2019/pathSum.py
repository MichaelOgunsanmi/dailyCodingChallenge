# Source: https://leetcode.com/problems/path-sum/
#
# Level: Easy
#
# Date: 02nd August 2019


"""Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values
along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""


# Solution


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, rootNode, val):
        return hasPathSumRec(rootNode, val, 0)


def hasPathSumRec(currentNode, val, currentSum):
    if currentNode is None:
        return False

    currentSum += currentNode.val

    if isLeaf(currentNode) and currentSum != val:
        return False

    if currentSum == val and isLeaf(currentNode):
        return True

    return hasPathSumRec(currentNode.left, val, currentSum) \
           or hasPathSumRec(currentNode.right, val, currentSum)


def isLeaf(currentNode):
    return currentNode.left is None and currentNode.right is None
