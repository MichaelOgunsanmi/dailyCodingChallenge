# Source: https://leetcode.com/problems/swap-nodes-in-pairs/
#
# Level: Medium
#
# Date: 29th July 2019


"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

"""


# Solution

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        firstNode = head
        secondNode = head.next
        newHead = head.next.next

        secondNode.next = firstNode

        firstNode.next = self.swapPairs(newHead)

        return secondNode
