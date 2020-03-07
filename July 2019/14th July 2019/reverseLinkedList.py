# Source: https://leetcode.com/problems/reverse-linked-list/

# Level: Easy

# Date: 14th July 2019

# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        if head is None:
            return head

        alreadyReversed = head
        currentNode = alreadyReversed.next
        alreadyReversed.next = None

        while currentNode is not None:
            storePointer = currentNode.next
            currentNode.next = alreadyReversed
            alreadyReversed = currentNode
            currentNode = storePointer

        return alreadyReversed
