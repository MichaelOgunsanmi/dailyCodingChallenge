# Source: https://leetcode.com/problems/validate-binary-search-tree/

# Level: Medium
#
# Date: 09th August 2019


"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""


# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, rootNode: TreeNode) -> bool:
        return isBST(rootNode, float('-inf'), float('inf'))


def isBST(currentNode, leftMin, rightMax):
    if currentNode is None:
        return True

    checkRoot = leftMin < currentNode.val < rightMax

    return checkRoot and isBST(currentNode.left, leftMin, currentNode.val) and isBST(currentNode.right, currentNode.val,
                                                                                     rightMax)
