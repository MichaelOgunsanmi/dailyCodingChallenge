# Source: https://leetcode.com/problems/lexicographical-numbers/

# Level: Medium

# Date: 21st July, 2019

# Given an integer n, return 1 - n in lexicographical order.
#
# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
#
# Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        answer = [str(i) for i in range(1, n + 1)]

        answer.sort()
        for i in range(len(answer)):
            answer[i] = int(answer[i])

        return answer
