# Source: https://leetcode.com/problems/add-digits/

# Level: Easy

# Date: 20th July, 2019

# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#
# Example:
#
# Input: 38
# Output: 2
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
# Since 2 has only one digit, return it.
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?

class Solution:
    def addDigits(self, num: int) -> int:
        sumValue = 0

        for i in str(num):
            sumValue += int(i)

        answer = (sumValue % 10) + (sumValue // 10)

        return answer if answer < 10 else (answer % 10) + (answer // 10)

        # return 9 if num % 9 == 0 and num > 0 else num % 9 # O(1) time
