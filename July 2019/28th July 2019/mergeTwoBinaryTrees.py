# Source: https://leetcode.com/problems/top-k-frequent-words/

# Level: Easy

# Date: 28th July 2019


"""Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees
are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up
as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7


Note: The merging process must start from the root nodes of both trees.
"""


# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, firstTree: TreeNode, secondTree: TreeNode) -> TreeNode:
        if firstTree is None:
            return secondTree

        if secondTree is None:
            return firstTree

        self.mergeTreesRec(firstTree, secondTree)

        return firstTree

    def mergeTreesRec(self, firstTree, secondTree):
        firstTree.val = firstTree.val + secondTree.val

        if firstTree.left is None and secondTree.left is not None:
            firstTree.left = secondTree.left
            if firstTree.right is None:
                if secondTree.right is not None:
                    firstTree.right = secondTree.right
                return

            if secondTree.right is not None:
                self.mergeTreesRec(firstTree.right, secondTree.right)

            return

        if firstTree.left is not None and secondTree.left is None:
            if firstTree.right is None:
                if secondTree.right is not None:
                    firstTree.right = secondTree.right
                return

            if secondTree.right is not None:
                self.mergeTreesRec(firstTree.right, secondTree.right)

            return

        if firstTree.left is not None and secondTree.left is not None:
            self.mergeTreesRec(firstTree.left, secondTree.left)

        if firstTree.right is None and secondTree.right is not None:
            firstTree.right = secondTree.right
            return

        if firstTree.right is not None and secondTree.right is None:
            return

        if firstTree.right is not None and secondTree.right is not None:
            self.mergeTreesRec(firstTree.right, secondTree.right)
