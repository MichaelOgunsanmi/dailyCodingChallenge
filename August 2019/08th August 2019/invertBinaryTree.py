# Source: https://leetcode.com/problems/invert-binary-tree/

# Level: Easy
#
# Date: 08th August 2019


"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a
whiteboard so f*** off. """


# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, rootNode: TreeNode) -> TreeNode:
        invert(rootNode)
        return rootNode


def invert(currentNode):
    if currentNode is None or isLeaf(currentNode):
        return

    swap(currentNode)

    if currentNode.left is not None:
        invert(currentNode.left)

    if currentNode.right is not None:
        invert(currentNode.right)

    return


def swap(currentNode):
    currentNode.left, currentNode.right = currentNode.right, currentNode.left


def isLeaf(currentNode):
    return currentNode.left is None and currentNode.right is None
