# Source: https://leetcode.com/problems/copy-list-with-random-pointer/
#
# Date: 18th August 2019


"""
A linked list is given such that each node contains an additional random pointer which could point to any node in
the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val,
random_index] where:

val: an integer representing Node.val random_index: the index of the node (range from 0 to n-1) where random pointer
points to, or null if it does not point to any node.


Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.


Constraints:

-10000 <= Node.val <= 10000
Node.random is null or pointing to a node in the linked list.
Number of Nodes will not exceed 1000.
"""


# Solution


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        currentNode = head

        while currentNode is not None:
            newNode = Node(currentNode.val)

            newNode.random = currentNode.random

            newNode.next = currentNode.next
            currentNode.next = newNode

            currentNode = currentNode.next.next

        currentNode = head.next

        while currentNode is not None:
            if currentNode.random is not None:
                currentNode.random = currentNode.random.next

            if currentNode.next is None:
                break
            currentNode = currentNode.next.next

        newHead = head.next

        originalCurrentNode = head
        newCurrentNode = head.next

        while newCurrentNode.next is not None:
            restOfOriginal = originalCurrentNode.next.next
            originalCurrentNode.next = restOfOriginal
            originalCurrentNode = restOfOriginal

            restOfNew = newCurrentNode.next.next
            newCurrentNode.next = restOfNew
            newCurrentNode = restOfNew

        originalCurrentNode.next = None
        newCurrentNode.next = None

        return newHead
