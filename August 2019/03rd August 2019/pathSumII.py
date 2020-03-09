# Source: https://leetcode.com/problems/path-sum-ii/
#
# Level: Medium
#
# Date: 03rd August 2019


"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
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
    def pathSum(self, rootNode: TreeNode, val: int) -> List[List[int]]:
        output = []
        pathSumRec(rootNode, val, 0, [], output)
        return output


def pathSumRec(currentNode, val, currentSum, treeElements, output):
    if currentNode is None:
        return

    currentSum += currentNode.val
    treeElements.append(currentNode.val)

    if isLeaf(currentNode) and currentSum != val:
        treeElements.pop()
        return

    if currentSum == val and isLeaf(currentNode):
        result = []
        result.extend(treeElements)
        output.append(result)
        treeElements.pop()
        return

    pathSumRec(currentNode.left, val, currentSum, treeElements, output)
    pathSumRec(currentNode.right, val, currentSum, treeElements, output)

    treeElements.pop()


def isLeaf(currentNode):
    return currentNode.left is None and currentNode.right is None
