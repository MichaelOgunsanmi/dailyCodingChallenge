# Source: https://leetcode.com/problems/linked-list-random-node/

# Level: Medium

# Date: 20th July, 2019

# Given a singly linked list, return a random node's value from the linked list. Each node must have the same
# probability of being chosen.
#
# Follow up: What if the linked list is extremely large and its length is unknown to you? Could you solve this
# efficiently without using extra space?
#
# Example:
#
# // Init a singly linked list [1,2,3].
# ListNode head = new ListNode(1);
# head.next = new ListNode(2);
# head.next.next = new ListNode(3);
# Solution solution = new Solution(head);
#
# // getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
# solution.getRandom();


from random import randrange


class Solution:

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.cur = head
        self.size = int(head is not None)
        while head.next is not None:
            self.size += 1
            head = head.next
        head.next = self.cur

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        steps = randrange(5)
        for _ in range(steps):
            self.cur = self.cur.next
        return self.cur.val
