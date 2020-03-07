# Source: https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Level: Easy

# Date: 28th July 2019


"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
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
    def maxDepth(self, root: TreeNode) -> int:
        return self.maxDepthRec(root, 1)

    def maxDepthRec(self, currentNode, count):
        if currentNode is None:
            return count - 1

        if isLeaf(currentNode):
            return count

        return max(self.maxDepthRec(currentNode.left, count + 1),
                   self.maxDepthRec(currentNode.right, count + 1))
