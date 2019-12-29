# Source: https://leetcode.com/problems/integer-to-roman/

# Level: Medium

# Date: 22nd July, 2019


# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII,
# which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not
# IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The
# same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
#
# Example 1:
#
# Input: 3
# Output: "III"
# Example 2:
#
# Input: 4
# Output: "IV"
# Example 3:
#
# Input: 9
# Output: "IX"
# Example 4:
#
# Input: 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
# Example 5:
#
# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


class Solution:
    def intToRoman(self, num: int) -> str:
        output = ""
        if num // 1000 > 0:
            check = num // 1000
            output += "M" * check
            num -= check * 1000

        if num // 100 > 0:
            check = num // 100
            output += converter(check, 'C', "CD", "D", "CM")
            num -= check * 100

        if num // 10 > 0:
            check = num // 10
            output += converter(check, 'X', "XL", "L", "XC")
            num -= check * 10

        output += converter(num, 'I', "IV", "V", "IX")

        return output


def converter(check, smallest, lessMid, mid, lessHigh):
    output = ""
    if check < 5:
        if check == 4:
            output += lessMid
        else:
            output += smallest * check
    elif check == 5:
        output += mid
    else:
        if check == 9:
            output += lessHigh
        else:
            remainder = check - 5
            output += mid
            output += smallest * remainder

    return output


