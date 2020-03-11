# Source: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Level: Easy
#
# Date: 08th August 2019


"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as
the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]




Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.


Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.
"""


# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, rootNode: 'TreeNode', firstNode: 'TreeNode', secondNode: 'TreeNode') -> 'TreeNode':
        firstAncestors = []
        getAncestors(rootNode, firstNode.val, firstAncestors)

        secondAncestors = []
        getAncestors(rootNode, secondNode.val, secondAncestors)

        firstIndex = len(firstAncestors) - 1
        secondIndex = len(secondAncestors) - 1

        while firstIndex >= 0 and secondIndex >= 0:
            if firstAncestors[firstIndex].val != secondAncestors[secondIndex].val:
                return firstAncestors[firstIndex + 1]

            firstIndex -= 1
            secondIndex -= 1

        if firstIndex == -1:
            return firstAncestors[0]

        if secondIndex == -1:
            return secondAncestors[0]


def getAncestors(currentNode, elementValue, ancestors):
    if currentNode is None:
        return

    if currentNode.val == elementValue:
        ancestors.append(currentNode)
        return

    if currentNode.val > elementValue:
        getAncestors(currentNode.left, elementValue, ancestors)
    else:
        getAncestors(currentNode.right, elementValue, ancestors)

    ancestors.append(currentNode)
