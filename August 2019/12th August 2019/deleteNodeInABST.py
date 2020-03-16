# Source: https://leetcode.com/problems/delete-node-in-a-bst/
#
# Date: 12th August 2019


"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root
node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
"""


# Solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deleteNode(self, rootNode: TreeNode, key: int) -> TreeNode:

        currentNode, parentNode = lookupNode(rootNode, None, key)

        if currentNode is None:
            return rootNode

        if isLeaf(currentNode):
            return removeLeaf(currentNode, parentNode, rootNode)

        if hasOneChild(currentNode):
            return removeNodeWithOneChild(currentNode, parentNode, rootNode)

        removeNodeWithTwoChildren(currentNode, rootNode)
        return rootNode


def lookupNode(currentNode, parentNode, key):
    while currentNode is not None:
        if currentNode.val == key:
            return (currentNode, parentNode)

        parentNode = currentNode

        if currentNode.val < key:
            currentNode = currentNode.right
        else:
            currentNode = currentNode.left

    return (currentNode, parentNode)


def isLeaf(currentNode):
    return currentNode.left is None and currentNode.right is None


def removeLeaf(currentNode, parentNode, rootNode):
    if parentNode is None:
        return None

    if parentNode.left is currentNode:
        parentNode.left = None
    else:
        parentNode.right = None

    return rootNode


def hasOneChild(currentNode):
    return (currentNode.left is None and currentNode.right is not None) or (
                currentNode.left is not None and currentNode.right is None)


def removeNodeWithOneChild(currentNode, parentNode, rootNode):
    if parentNode is None:
        if currentNode.left is not None:
            return currentNode.left
        else:
            return currentNode.right

    if parentNode.left is currentNode:
        if currentNode.left is None:
            parentNode.left = currentNode.right
        else:
            parentNode.left = currentNode.left
    else:
        if currentNode.left is None:
            parentNode.right = currentNode.right
        else:
            parentNode.right = currentNode.left

    return rootNode


def removeNodeWithTwoChildren(currentNode, rootNode):
    predecessor = currentNode
    successor = currentNode.right

    while successor.left is not None:
        predecessor = successor
        successor = successor.left

    currentNode.val = successor.val

    if isLeaf(successor):
        removeLeaf(successor, predecessor, rootNode)
    else:
        removeNodeWithOneChild(successor, predecessor, rootNode)
