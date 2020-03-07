# Source: https://leetcode.com/problems/powx-n/submissions/
#
# Level: Easy
#
# Date: 30th July 2019


"""
Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \
    1   3

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, and each node's value is different.
This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
"""


# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if root is None or isLeaf(root):
            return 0
        treeElements = minDiff(root, [float('inf')])

        if len(treeElements) == 3:
            if abs(treeElements[1] - treeElements[2]) < treeElements[0]:
                treeElements[0] = abs(treeElements[1] - treeElements[2])
            treeElements.pop(1)

        return treeElements[0]


def minDiff(currentNode, treeElements):
    if currentNode.left is not None:
        minDiff(currentNode.left, treeElements)

    if len(treeElements) == 3:
        if abs(treeElements[1] - treeElements[2]) < treeElements[0]:
            treeElements[0] = abs(treeElements[1] - treeElements[2])
        treeElements.pop(1)

    treeElements.append(currentNode.val)

    if currentNode.right is not None:
        minDiff(currentNode.right, treeElements)

    return treeElements


def isLeaf(currentNode):
    return currentNode.left is None and currentNode.right is None
