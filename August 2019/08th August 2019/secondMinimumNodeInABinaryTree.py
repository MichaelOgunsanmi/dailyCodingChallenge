# Source: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

# Level: Easy
#
# Date: 08th August 2019


"""Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this
tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value
among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the
whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input:
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.


Example 2:

Input:
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
"""


# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, rootNode: TreeNode) -> int:
        if isLeaf(rootNode):
            return -1

        minimumValues = [float('inf'), float('inf')]

        findMinimums(rootNode, minimumValues)

        print(minimumValues)
        if minimumValues[0] == minimumValues[1] or minimumValues[1] == float('inf'):
            return -1
        else:
            return minimumValues[1]


def findMinimums(currentNode, minimumValues):
    checkMinimums(currentNode, minimumValues)

    if isLeaf(currentNode):
        return

    findMinimums(currentNode.left, minimumValues)
    findMinimums(currentNode.right, minimumValues)

    return


def checkMinimums(currentNode, minimumValues):
    if currentNode.val not in minimumValues and currentNode.val < minimumValues[1]:
        minimumValues[1] = currentNode.val

        if minimumValues[1] < minimumValues[0]:
            minimumValues[0], minimumValues[1] = minimumValues[1], minimumValues[0]


def isLeaf(currentNode):
    return currentNode.left is None and currentNode.right is None
