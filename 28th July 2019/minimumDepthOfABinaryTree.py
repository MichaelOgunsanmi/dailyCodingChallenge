# Source: https://leetcode.com/problems/top-k-frequent-words/

# Level: Easy

# Date: 28th July, 2019


"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""


# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isLeaf(currentNode):
    return currentNode.left is None and currentNode.right is None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return self.minDepthRec(root, 1)

    def minDepthRec(self, currentNode, count):
        if currentNode is None:
            return float('inf')

        if isLeaf(currentNode):
            return count

        return min(self.minDepthRec(currentNode.left, count + 1),
                   self.minDepthRec(currentNode.right, count + 1))
