-- Source: https://leetcode.com/problems/nth-highest-salary/

-- Level: Medium

-- Date: 07th July 2019, 2019


-- Write a SQL query to get the nth highest salary from the Employee table.

-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.

-- +------------------------+
-- | getNthHighestSalary(2) |
-- +------------------------+
-- | 200                    |
-- +------------------------+

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE getNthHighestValue INT;
    DECLARE K INT;
    SET K = N-1;
    SELECT IFNULL((SELECT 
    DISTINCT Salary
    FROM Employee
    ORDER BY Salary DESC
    LIMIT K,1), NULL) INTO getNthHighestValue;
  RETURN getNthHighestValue;
END
