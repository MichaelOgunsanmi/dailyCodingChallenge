# Source: https://leetcode.com/problems/binary-tree-inorder-traversal/
#
# Date: 12th August 2019


"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
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
    def inorderTraversal(self, rootNode: TreeNode) -> List[int]:
        if rootNode is None:
            return []

        treeElements = []
        stack = []
        currentNode = rootNode

        while len(stack) != 0 or currentNode is not None:
            if currentNode is not None:
                stack.append(currentNode)
                currentNode = currentNode.left
            else:
                currentNode = stack.pop()
                treeElements.append(currentNode.val)
                currentNode = currentNode.right

        return treeElements
