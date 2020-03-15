# Source: https://leetcode.com/problems/delete-leaves-with-a-given-value/
#
# Level: Medium
#
# Date: 10th August 2019


"""
Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if it's parent node becomes a leaf node and has the value
target, it should also be deleted (you need to continue doing that until you can't).



Example 1:



Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left).
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).
Example 2:



Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]
Example 3:



Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.
Example 4:

Input: root = [1,1,1], target = 1
Output: []
Example 5:

Input: root = [1,2,3], target = 1
Output: [1,2,3]


Constraints:

1 <= target <= 1000
Each tree has at most 3000 nodes.
Each node's value is between [1, 1000].
"""


# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def removeLeafNodes(self, rootNode: TreeNode, target: int) -> TreeNode:
        if rootNode is None:
            return None

        parentNode = TreeNode(None)
        parentNode.left = rootNode

        removeTargets(rootNode, parentNode, target)

        if parentNode.left is None:
            return None
        else:
            return parentNode.left


def removeTargets(currentNode, parentNode, target):
    if isLeaf(currentNode) and currentNode.val == target:
        if parentNode.left == currentNode:
            parentNode.left = None
        else:
            parentNode.right = None

        return

    if currentNode.left is not None:
        removeTargets(currentNode.left, currentNode, target)

    if currentNode.right is not None:
        removeTargets(currentNode.right, currentNode, target)

    if isLeaf(currentNode) and currentNode.val == target:
        removeTargets(currentNode, parentNode, target)


def isLeaf(currentNode):
    return currentNode.left is None and currentNode.right is None
