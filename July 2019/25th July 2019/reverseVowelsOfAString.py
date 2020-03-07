# Source: https://leetcode.com/problems/reverse-vowels-of-a-string/

# Level: Easy

# Date: 25th July 2019, 2019

# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
#
# Input: "hello"
# Output: "holle"
# Example 2:
#
# Input: "leetcode"
# Output: "leotcede"
# Note:
# The vowels does not include the letter "y".


class Solution:
    def reverseVowels(self, stringInput: str) -> str:
        frontPointer = 0
        backPointer = len(stringInput) - 1
        stringInput = list(stringInput)

        while frontPointer < backPointer:
            if stringInput[frontPointer] not in 'aeiouAEIOU' or stringInput[backPointer] not in 'aeiouAEIOU':
                if stringInput[frontPointer] not in 'aeiouAEIOU':
                    frontPointer += 1

                if stringInput[backPointer] not in 'aeiouAEIOU':
                    backPointer -= 1
            else:
                stringInput[frontPointer], stringInput[backPointer] = stringInput[backPointer], stringInput[
                    frontPointer]
                frontPointer += 1
                backPointer -= 1

        return "".join(stringInput)
