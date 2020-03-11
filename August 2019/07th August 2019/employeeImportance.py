# Source: https://leetcode.com/problems/employee-importance/

# Level: Easy
#
# Date: 07th August 2019


"""You are given a data structure of employee information, which includes the employee's unique id, his importance
value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance
value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10,
[3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1,
the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of
this employee and all his subordinates.

Example 1:

Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1 Output: 11 Explanation: Employee 1 has importance value 5,
and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total
importance value of employee 1 is 5 + 3 + 3 = 11.


Note:

One employee has at most one direct leader and may have several subordinates.
The maximum number of employees won't exceed 2000.
"""

# Solution
from typing import List


# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hashMap = {}

        for employee in employees:
            hashMap[employee.id] = [employee.importance, employee.subordinates]

        subordinates = hashMap[id][1]
        empVal = hashMap[id][0]
        queue = []
        queue.extend(subordinates)

        while len(queue) != 0:
            sub = queue.pop(0)
            empVal += hashMap[sub][0]
            newSubs = hashMap[sub][1]

            for subs in newSubs:
                if subs not in queue:
                    queue.append(subs)

        return empVal
