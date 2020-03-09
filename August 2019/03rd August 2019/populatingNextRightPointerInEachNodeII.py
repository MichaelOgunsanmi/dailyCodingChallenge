# Source: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
#
# Level: Medium
#
# Date: 03rd August 2019


"""
Given a binary tree

struct Node { int val; Node *left; Node *right; Node *next; } Populate each next pointer to point to its next right
node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


Example 1:



Input: root = [1,2,3,4,5,null,7] Output: [1,#,2,3,#,4,5,7,#] Explanation: Given the above binary tree (Figure A),
your function should populate each next pointer to point to its next right node, just like in Figure B. The
serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


Constraints:

The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100
"""


# Solution


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, rootNode: 'Node') -> 'Node':
        if rootNode is None:
            return rootNode

        queue = [rootNode]
        size = 1
        curSize = 0

        while len(queue) != 0:
            currentNode = queue.pop(0)
            size -= 1

            if currentNode.left is not None:
                queue.append(currentNode.left)
                curSize += 1

            if currentNode.right is not None:
                queue.append(currentNode.right)
                curSize += 1

            if size != 0:
                currentNode.next = queue[0]
            else:
                size = curSize
                curSize = 0

        return rootNode
