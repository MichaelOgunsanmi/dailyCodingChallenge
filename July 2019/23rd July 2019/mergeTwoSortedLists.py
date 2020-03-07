# Source: https://leetcode.com/problems/merge-two-sorted-lists/

# Level: Easy

# Date: 23rd July 2019, 2019

# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the
# nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, firstHead, secondHead):
        firstPointer = firstHead
        secondPointer = secondHead

        if firstPointer is None:
            return secondPointer

        if secondPointer is None:
            return firstPointer

        if firstPointer.val < secondPointer.val:
            currentPointer = firstPointer
            firstPointer = firstPointer.next
        else:
            currentPointer = secondPointer
            secondPointer = secondPointer.next

        head = currentPointer

        while firstPointer is not None and secondPointer is not None:
            if firstPointer.val > secondPointer.val:
                currentPointer.next = secondPointer
                secondPointer = secondPointer.next
            else:
                currentPointer.next = firstPointer
                firstPointer = firstPointer.next

            currentPointer = currentPointer.next

        if firstPointer is None:
            currentPointer.next = secondPointer
        else:
            currentPointer.next = firstPointer

        return head
