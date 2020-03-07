# Source: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Level: Easy

# Date: 12th July 2019, 2019

# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# Example 1:
#
# Input: 1->1->2
# Output: 1->2
# Example 2:
#
# Input: 1->1->2->3->3
# Output: 1->2->3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return

        firstPointer = head
        secondPointer = head.next

        while secondPointer is not None:
            if firstPointer.val == secondPointer.val:
                firstPointer.next = secondPointer.next
                secondPointer.next = None
                secondPointer = firstPointer.next
            else:
                firstPointer = firstPointer.next
                secondPointer = secondPointer.next

        return head
