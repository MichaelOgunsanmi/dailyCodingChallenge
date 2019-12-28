# Source: https://leetcode.com/problems/student-attendance-record-i/

# Level: Easy

# Date: 21st July, 2019

# You are given a string representing an attendance record for a student. The record only contains the following
# three characters: 'A' : Absent. 'L' : Late. 'P' : Present. A student could be rewarded if his attendance record
# doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
#
# You need to return whether the student could be rewarded according to his attendance record.
#
# Example 1:
# Input: "PPALLP"
# Output: True
# Example 2:
# Input: "PPALLL"
# Output: False


class Solution:
    def checkRecord(self, stringInput: str) -> bool:
        if len(stringInput) <= 1:
            return True
        couldBeRewarded = True
        absent = 0
        doubleL = False

        for index, attendance in enumerate(stringInput):
            if attendance == 'A':
                absent += 1

            if attendance == 'L' and stringInput[index - 1] == 'L' and stringInput[
                index - 2] == 'L' and index - 1 >= 0 and index - 2 >= 0:
                doubleL = True

        if absent > 1 or doubleL:
            couldBeRewarded = False

        return couldBeRewarded
