# Source: https://leetcode.com/problems/count-and-say/

# Level: Easy

# Date: 13th July 2019

# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
#
# Note: Each term of the sequence of integers will be represented as a string.
#
#
#
# Example 1:
#
# Input: 1
# Output: "1"
# Example 2:
#
# Input: 4
# Output: "1211"

class Solution:
    def countAndSay(self, n: int):
        if n == 1:
            return "1"

        i = 0
        prev = "1"
        while i < n-1:
            i += 1
            output = ""
            j = 0
            count = 0
            while j < len(prev):
                if j == len(prev) - 1:
                    if prev[j] == prev[j - 1]:
                        count += 1
                    else:
                        count = 1
                    num = prev[j]
                elif j == 0:
                    if prev[j] == prev[j+1]:
                        count += 1
                        num = prev[j]
                        j += 1
                        continue
                    else:
                        count = 1
                        num = prev[j]
                else:
                    if prev[j] == prev[j+1]:
                        count += 1
                        num = prev[j]
                        j += 1
                        continue
                    else:
                        if prev[j] == prev[j - 1]:
                            count += 1
                        else:
                            count = 1
                            num = prev[j]
                k = 0
                output += str(count)
                output += num
                count = 0
                j += 1
            prev = output

        return output