-- Source: https://leetcode.com/problems/employees-earning-more-than-their-managers/

-- Level: Easy

-- Date: 8th July, 2019


-- SQL Schema
-- The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

-- +----+-------+--------+-----------+
-- | Id | Name  | Salary | ManagerId |
-- +----+-------+--------+-----------+
-- | 1  | Joe   | 70000  | 3         |
-- | 2  | Henry | 80000  | 4         |
-- | 3  | Sam   | 60000  | NULL      |
-- | 4  | Max   | 90000  | NULL      |
-- +----+-------+--------+-----------+
-- Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.

-- +----------+
-- | Employee |
-- +----------+
-- | Joe      |
-- +----------+

-- # Write your MySQL query statement below

SELECT E.Name as Employee
FROM Employee E
JOIN Employee M
ON M.Id = E.ManagerId
WHERE E.Salary > M.Salary