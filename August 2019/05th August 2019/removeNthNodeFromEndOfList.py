# Source: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Level: Medium
#
# Date: 05th August 2019


"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""


# Solution

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None

        frontPointer = head
        endPointer = head
        count = 0

        while count < n - 1:
            count += 1
            endPointer = endPointer.next

        if endPointer.next is None:
            return frontPointer.next

        while endPointer.next.next is not None:
            endPointer = endPointer.next
            frontPointer = frontPointer.next

        frontPointer.next = frontPointer.next.next

        return head
