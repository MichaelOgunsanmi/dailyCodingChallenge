# Source: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
#
# Date: 14th August 2019


"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""


# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, rootNode: TreeNode) -> None:
        if rootNode is None:
            return rootNode

        preOrderTraversal = []

        doPreOrderTraversal(rootNode, preOrderTraversal)

        index = 0

        while index < len(preOrderTraversal) - 1:
            preOrderTraversal[index].left = None
            preOrderTraversal[index].right = preOrderTraversal[index + 1]
            index += 1

        preOrderTraversal[index].left = None
        preOrderTraversal[index].right = None


def doPreOrderTraversal(currentNode, treeElements):
    treeElements.append(currentNode)

    if currentNode.left is not None:
        doPreOrderTraversal(currentNode.left, treeElements)

    if currentNode.right is not None:
        doPreOrderTraversal(currentNode.right, treeElements)
