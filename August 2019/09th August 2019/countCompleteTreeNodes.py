# Source: https://leetcode.com/problems/count-complete-tree-nodes/

# Level: Medium
#
# Date: 09th August 2019


"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia: In a complete binary tree every level, except possibly the last,
is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes
inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""


# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, rootNode: TreeNode) -> int:
        if rootNode is None:
            return 0

        if isLeaf(rootNode):
            return 1

        return 1 + self.countNodes(rootNode.left) + self.countNodes(rootNode.right)


def isLeaf(currentNode):
    return currentNode.left is None and currentNode.right is None
