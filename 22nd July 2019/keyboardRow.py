# Source: https://leetcode.com/problems/keyboard-row/

# Level: Easy

# Date: 22nd July, 2019


# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American
# keyboard like the image below.
#
#
#
#
#
#
# Example:
#
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
#
#
# Note:
#
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        true = True
        firstRow = {'q': true, 'w': true, 'e': true, 'r': true, 't': true, 'y': true, 'u': true, 'i': true, 'o': true,
                    'p': true}
        secondRow = {'a': true, 's': true, 'd': true, 'f': true, 'g': true, 'h': true, 'j': true, 'k': true, 'l': true}
        thirdRow = {'z': true, 'x': true, 'c': true, 'v': true, 'b': true, 'n': true, 'm': true}

        output = []

        for word in words:
            firstLetter = word[0].lower()
            checkingRow = firstRow if firstLetter in firstRow else secondRow if firstLetter in secondRow else thirdRow
            allIn = True

            for letter in word.lower():
                if letter not in checkingRow:
                    allIn = False
                    break

            if allIn:
                output.append(word)

        return output
