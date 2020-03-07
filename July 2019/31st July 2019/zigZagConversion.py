# Source: https://leetcode.com/problems/zigzag-conversion/
#
# Level: Medium
#
# Date: 31st July 2019, 2019


"""The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to
display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""


# Solution

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        countVariable = 2 * (numRows - 1)
        countPoint = 0
        output = ''
        i = 0

        while i < len(s):
            firstSequence = countVariable - (2 * countPoint)

            if countVariable == firstSequence or firstSequence == 0:
                firstSequence = secondSequence = countVariable
            else:
                secondSequence = countVariable - firstSequence

            j = countPoint

            while j < len(s):
                output += s[j]
                i += 1

                if j + firstSequence < len(s):
                    output += s[j + firstSequence]
                    i += 1

                j += firstSequence

                if firstSequence == countVariable:
                    j += firstSequence
                else:
                    j += secondSequence

            countPoint += 1

        return output
