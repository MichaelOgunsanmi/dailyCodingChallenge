# Source: https://leetcode.com/problems/subtree-of-another-tree/
#
# Date: 18th August 2019


"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with
a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could
also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""


# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, mainTree: TreeNode, testTree: TreeNode) -> bool:
        treeNodes = []
        inOrderTraversal(mainTree, treeNodes)

        for node in treeNodes:
            isSub = isSameTree(testTree, node)

            if isSub:
                return True

        return False


def inOrderTraversal(currentNode, treeElements):
    if currentNode.left is not None:
        inOrderTraversal(currentNode.left, treeElements)

    treeElements.append(currentNode)

    if currentNode.right is not None:
        inOrderTraversal(currentNode.right, treeElements)


def isSameTree(mainTree, testTree):
    if mainTree is None and testTree is None:
        return True

    if (mainTree is None and testTree is not None) or (mainTree is not None and testTree is None):
        return False

    if mainTree.val != testTree.val:
        return False

    return isSameTree(mainTree.left, testTree.left) and isSameTree(mainTree.right, testTree.right)
