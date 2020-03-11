# Source: https://leetcode.com/problems/cousins-in-binary-tree/

# Level: Easy
#
# Date: 07th August 2019


"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.



Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false


Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
"""


# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isCousins(self, rootNode: TreeNode, x: int, y: int) -> bool:
        if rootNode is None:
            return False

        collector = {'xDepth': 0, 'xParent': None, 'yDepth': 0, 'yParent': None}
        lookup(rootNode, x, y, 0, collector)

        # print(collector)

        xParent = collector['xParent']
        xDepth = collector['xDepth']
        yDepth = collector['yDepth']
        yParent = collector['yParent']

        if xParent == yParent or xDepth != yDepth:
            return False

        return True


def lookup(currentNode, xTarget, yTarget, depth, collector):
    if currentNode is None:
        return

    if (hasLeftNode(currentNode) and nodeVal(currentNode.left) == xTarget) \
            or (hasRightNode(currentNode) and nodeVal(currentNode.right) == xTarget):
        collector['xParent'] = currentNode
        collector['xDepth'] = depth + 1

    if (hasLeftNode(currentNode) and nodeVal(currentNode.left) == yTarget) \
            or (hasRightNode(currentNode) and nodeVal(currentNode.right) == yTarget):
        collector['yParent'] = currentNode
        collector['yDepth'] = depth + 1

    if hasLeftNode(currentNode):
        lookup(currentNode.left, xTarget, yTarget, depth + 1, collector)

    if hasRightNode(currentNode):
        lookup(currentNode.right, xTarget, yTarget, depth + 1, collector)

    return


def hasLeftNode(currentNode):
    return currentNode.left is not None


def hasRightNode(currentNode):
    return currentNode.right is not None


def nodeVal(currentNode):
    return currentNode.val
