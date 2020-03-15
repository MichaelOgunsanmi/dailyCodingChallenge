# Source: https://leetcode.com/problems/binary-tree-preorder-traversal/

# Level: Medium
#
# Date: 11th August 2019


"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
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
    def preorderTraversal(self, rootNode: TreeNode) -> List[int]:
        if rootNode is None:
            return []

        treeElements = []
        stack = [rootNode]
        currentNode = rootNode

        while len(stack) != 0:
            currentNode = stack.pop()
            treeElements.append(currentNode.val)

            if currentNode.right is not None:
                stack.append(currentNode.right)

            if currentNode.left is not None:
                stack.append(currentNode.left)

        return treeElements
