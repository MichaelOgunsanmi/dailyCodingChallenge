# Source: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Level: Medium
#
# Date: 09th August 2019


"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up: What if the BST is
modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize
the kthSmallest routine?
"""


# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, rootNode: TreeNode, k: int) -> int:
        if rootNode is None:
            return rootNode

        ans = [k]
        elements = []
        inOrder(rootNode, ans, [False], elements)
        return elements[0]


def inOrder(currentNode, counter, found, ans):
    if found[0]:
        return

    if currentNode.left is not None:
        inOrder(currentNode.left, counter, found, ans)

    counter[0] -= 1
    if counter[0] == 0:
        found[0] = True
        ans.append(currentNode.val)

        return
    if currentNode.right is not None:
        inOrder(currentNode.right, counter, found, ans)
