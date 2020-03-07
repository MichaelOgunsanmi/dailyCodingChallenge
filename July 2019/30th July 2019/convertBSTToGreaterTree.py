# Source: https://leetcode.com/problems/convert-bst-to-greater-tree/
#
# Level: Easy
#
# Date: 30th July 2019, 2019


"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
"""


# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        binaryToGreater(root, [0])
        return root


def binaryToGreater(currentNode, val):
    if currentNode.right is not None:
        binaryToGreater(currentNode.right, val)

    currentNode.val += val[0]
    val[0] = currentNode.val

    if currentNode.left is not None:
        binaryToGreater(currentNode.left, val)

    return
