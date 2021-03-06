# Source: https://leetcode.com/problems/valid-parentheses/

# Level: Easy

# Date: 23rd July 2019

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false
# Example 5:
#
# Input: "{[]}"
# Output: true


class Solution:
    def isValid(self, stringInput: str) -> bool:
        stack = []

        for index, character in enumerate(stringInput):
            if isOpenBracket(character):
                stack.append(character)
            else:
                if len(stack) == 0:
                    return False
                frontCharacter = stack.pop()
                if not isSamePair(frontCharacter, character):
                    return False
        return len(stack) == 0


def isOpenBracket(character):
    return character == '(' or character == '{' or character == '['


def isSamePair(frontCharacter, backCharacter):
    if frontCharacter == '{':
        return backCharacter == '}'
    if frontCharacter == '(':
        return backCharacter == ')'
    if frontCharacter == '[':
        return backCharacter == ']'
