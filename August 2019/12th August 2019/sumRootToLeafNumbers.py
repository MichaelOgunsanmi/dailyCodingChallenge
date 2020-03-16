# Source: https://leetcode.com/problems/sum-root-to-leaf-numbers/
#
# Date: 12th August 2019


"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""


# Solution

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, rootNode: TreeNode) -> int:
        sumVal = [0]

        getSum(rootNode, sumVal, '')

        return sumVal[0]


def getSum(currentNode, sumVal, accumulator):
    if currentNode is None:
        return

    if isLeaf(currentNode):
        value = accumulator + str(currentNode.val)
        sumVal[0] += int(value)
        return

    newAccumulator = accumulator + str(currentNode.val)

    if currentNode.left is not None:
        getSum(currentNode.left, sumVal, newAccumulator)

    if currentNode.right is not None:
        getSum(currentNode.right, sumVal, newAccumulator)


def isLeaf(currentNode):
    return currentNode.left is None and currentNode.right is None
