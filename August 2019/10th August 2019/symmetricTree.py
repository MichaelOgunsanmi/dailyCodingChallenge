# Source: https://leetcode.com/problems/symmetric-tree/

# Level: Easy
#
# Date: 10th August 2019


"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Note:
Bonus points if you could solve it both recursively and iteratively.
"""


# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, rootNode: TreeNode) -> bool:
        if rootNode is None:
            return True

        return checkSymmetry(rootNode.left, rootNode.right)


def checkSymmetry(firstNode, secondNode):
    if firstNode is None and secondNode is None:
        return True

    if (firstNode is None and secondNode is not None) or (firstNode is not None and secondNode is None):
        return False

    if firstNode.val != secondNode.val:
        return False

    return checkSymmetry(firstNode.left, secondNode.right) and checkSymmetry(firstNode.right, secondNode.left)
