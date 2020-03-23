# Source: https://leetcode.com/problems/merge-intervals/
#
# Date: 18th August 2019


"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]] Output: [[1,5]] Explanation: Intervals [1,4] and [4,5] are considered overlapping. NOTE: input
types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
 """


# Solution
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0 or len(intervals[0]) == 0:
            return []

        intervals.sort(key=lambda x: x[0])

        output = []
        currentStartTime = intervals[0][0]
        currentEndTime = intervals[0][1]
        intervalPosition = 1

        while intervalPosition < len(intervals):
            timePoint = 0
            while timePoint < 2:
                if intervals[intervalPosition][timePoint] <= currentStartTime:
                    currentStartTime = intervals[intervalPosition][timePoint]

                if intervals[intervalPosition][timePoint] <= currentEndTime:
                    timePoint += 1
                else:
                    if timePoint == 1:
                        currentEndTime = intervals[intervalPosition][timePoint]

                        if intervalPosition + 1 < len(intervals) and intervals[intervalPosition + 1][0] <= \
                                intervals[intervalPosition][1]:
                            break
                        else:
                            output.append([currentStartTime, currentEndTime])
                            if intervalPosition + 1 < len(intervals):
                                intervalPosition += 1
                                currentStartTime = intervals[intervalPosition][0]
                                currentEndTime = intervals[intervalPosition][1]
                            else:
                                currentStartTime = intervals[intervalPosition][0]
                                currentEndTime = intervals[intervalPosition][1]
                                break
                    else:
                        output.append([currentStartTime, currentEndTime])
                        if intervalPosition + 1 < len(intervals):
                            currentStartTime = intervals[intervalPosition][0]
                            currentEndTime = intervals[intervalPosition][1]
                            intervalPosition += 1
                        else:
                            currentStartTime = intervals[intervalPosition][0]
                            currentEndTime = intervals[intervalPosition][1]
                            break
            intervalPosition += 1

        if len(output) == 0 or currentEndTime != output[len(output) - 1][1]:
            output.append([currentStartTime, currentEndTime])

        return output
