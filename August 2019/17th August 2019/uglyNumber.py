# Source: https://leetcode.com/problems/ugly-number/
#
# Date: 17th August 2019


"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:

1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−231,  231 − 1].
"""


# Solution


class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 1:
            return True

        ugly = [1]
        t1, t2, t3 = 0, 0, 0

        while ugly[-1] < num:
            # print(t1, t2, t3)
            u1 = 2 * ugly[t1]
            u2 = 3 * ugly[t2]
            u3 = 5 * ugly[t3]

            umin = min(u1, u2, u3)

            if umin == num:
                return True

            if umin == u1:
                t1 += 1

            if umin == u2:
                t2 += 1

            if umin == u3:
                t3 += 1

            ugly.append(umin)

        return False
