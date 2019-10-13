'''
Source: https://leetcode.com/problems/palindrome-number/

Level: Easy

Date: 6th July, 2019

'''

'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
'''
#Solution

class Solution:
    def isPalindrome(self, number):
        if number < 0:
            return False
        if number == 0:
            return True 

        x = math.floor(math.log10(number))
        while number > 0:
            front, back = number // 10 ** x, number % 10
            if front != back:
                return False
            number = int (number - (front * (10 ** x) + back)) / 10
            x -= 2

        return True

class Solution2:
    def isPalindrome(self, number):
        if number < 0:
            return False
        return True if int(str(number)[::-1]) == number else False
        