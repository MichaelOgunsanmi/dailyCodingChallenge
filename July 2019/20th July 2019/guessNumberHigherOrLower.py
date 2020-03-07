# Source: https://leetcode.com/problems/guess-number-higher-or-lower/

# Level: Easy

# Date: 20th July 2019

# We are playing the Guess Game. The game is as follows:
#
# I pick a number from 1 to n. You have to guess which number I picked.
#
# Every time you guess wrong, I'll tell you whether the number is higher or lower.
#
# You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
#
# -1 : My number is lower
# 1 : My number is higher
# 0 : Congrats! You got it!
# Example :
#
# Input: n = 10, pick = 6
# Output: 6

# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


def guess(num):
    val = 6
    if num == val:
        return 0
    if num < val:
        return 1

    if num > val:
        return -1


class Solution:
    def guessNumber(self, n: int) -> int:
        firstNumber = 1
        lastNumber = n + 1
        pick = (lastNumber - firstNumber) // 2
        answer = guess(pick)

        while answer != 0:
            if answer == 1:
                firstNumber = pick
                pick = firstNumber + (lastNumber - firstNumber) // 2
            elif answer == -1:
                lastNumber = pick
                pick = firstNumber + (lastNumber - firstNumber) // 2

            answer = guess(pick)

        return pick
