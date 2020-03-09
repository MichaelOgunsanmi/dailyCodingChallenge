# Source: https://leetcode.com/problems/binary-tree-right-side-view/
#
# Level: Medium
#
# Date: 03rd August 2019


"""Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see
ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""


# Solution

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, rootNode: TreeNode) -> List[int]:
        if rootNode is None:
            return []

        queue = [rootNode]
        treeElements = []

        while len(queue) != 0:
            siblings = queue
            queue = []
            treeElements.append(siblings[len(siblings) - 1].val)

            while len(siblings) != 0:
                currentNode = siblings.pop(0)

                if currentNode.left is not None:
                    queue.append(currentNode.left)

                if currentNode.right is not None:
                    queue.append(currentNode.right)

        return treeElements

#       #method 2
#         return rightSideRec(rootNode, [])


# def rightSideRec(currentNode, treeElements):
#     if currentNode is None:
#         return treeElements

#     treeElements.append(currentNode.val)

#     if currentNode.right is not None:
#         rightSideRec(currentNode.right, treeElements)

#     else:
#         rightSideRec(currentNode.left, treeElements)

#     return treeElements
