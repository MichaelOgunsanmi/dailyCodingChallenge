# Source: https://leetcode.com/problems/same-tree/

# Level: Easy
#
# Date: 09th August 2019


"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""


# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, firstTree: TreeNode, secondTree: TreeNode) -> bool:
        if firstTree is None and secondTree is None:
            return True

        if (firstTree is None and secondTree is not None) or (firstTree is not None and secondTree is None):
            return False

        if firstTree.val != secondTree.val:
            return False

        return self.isSameTree(firstTree.left, secondTree.left) and self.isSameTree(firstTree.right, secondTree.right)
