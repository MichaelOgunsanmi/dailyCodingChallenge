# Source: https://leetcode.com/problems/insert-into-a-binary-search-tree/
#
# Date: 13th August 2019


"""Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into
the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in
the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion.
You can return any of them.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \
    1   3
         \
          4
"""


# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoBST(self, rootNode: TreeNode, val: int) -> TreeNode:
        newNode = TreeNode(val)

        if rootNode is None:
            rootNode = newNode
            return rootNode

        currentNode = rootNode

        while currentNode is not None:
            if currentNode.val < val:
                if currentNode.right is None:
                    currentNode.right = newNode
                    return rootNode
                currentNode = currentNode.right
            else:
                if currentNode.left is None:
                    currentNode.left = newNode
                    return rootNode

                currentNode = currentNode.left
