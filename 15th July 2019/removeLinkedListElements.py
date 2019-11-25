# Source: https://leetcode.com/problems/remove-linked-list-elements/

# Level: Easy

# Date: 15th July, 2019

# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head

        currentNode = head
        while currentNode is not None and currentNode.val == val:
            currentNode = currentNode.next

        head = currentNode
        prevNode = head
        if currentNode is None:
            return head
        currentNode = currentNode.next

        while currentNode is not None:
            if currentNode.val != val:
                prevNode.next = currentNode
                prevNode = currentNode

            currentNode = currentNode.next

        prevNode.next = None

        return head
