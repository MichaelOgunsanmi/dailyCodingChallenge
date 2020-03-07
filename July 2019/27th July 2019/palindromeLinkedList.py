# Source: https://leetcode.com/problems/palindrome-linked-list/

# Level: Easy

# Date: 27th July 2019, 2019


# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
# Example 2:
#
# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head) -> bool:
        if head is None or head.next is None:
            return True

        fastPointer = head.next
        slowPointer = fastPointer
        alreadyReversed = head
        alreadyReversed.next = None

        while fastPointer.next is not None and fastPointer.next.next is not None:
            fastPointer = fastPointer.next.next
            holder = slowPointer
            slowPointer = slowPointer.next
            holder.next = alreadyReversed
            alreadyReversed = holder

        if fastPointer.next is not None:
            slowPointer = slowPointer.next

        while slowPointer is not None:
            if slowPointer.val != alreadyReversed.val:
                return False

            slowPointer = slowPointer.next
            alreadyReversed = alreadyReversed.next

        return True
