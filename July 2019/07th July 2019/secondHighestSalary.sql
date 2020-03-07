-- Source: https://leetcode.com/problems/second-highest-salary/

-- Level: Easy

-- Date: 07th July 2019, 2019

-- SQL Schema
-- Write a SQL query to get the second highest salary from the Employee table.

-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | 200                 |
-- +---------------------+

--Write your MySQL query statement below

SELECT
    CASE 
        WHEN COUNT(Salary) > 1  THEN (SELECT Salary
        FROM Employee
        GROUP BY Salary DESC LIMIT 1,1)
        ELSE null
    END as SecondHighestSalary
    
FROM (
    SELECT *
    FROM Employee
    GROUP BY Salary DESC
) AS C
