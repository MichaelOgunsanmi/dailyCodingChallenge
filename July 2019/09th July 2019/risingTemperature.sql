-- Source: https://leetcode.com/problems/rising-temperature/

-- Level: Easy

-- Date: 09th July 2019, 2019

-- SQL Schema
-- Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.

-- +---------+------------------+------------------+
-- | Id(INT) | RecordDate(DATE) | Temperature(INT) |
-- +---------+------------------+------------------+
-- |       1 |       2015-01-01 |               10 |
-- |       2 |       2015-01-02 |               25 |
-- |       3 |       2015-01-03 |               20 |
-- |       4 |       2015-01-04 |               30 |
-- +---------+------------------+------------------+
-- For example, return the following Ids for the above Weather table:

-- +----+
-- | Id |
-- +----+
-- |  2 |
-- |  4 |
-- +----+

# Write your MySQL query statement below
SELECT c.Id
FROM Weather c
JOIN Weather p ON c.RecordDate = DATE_ADD(p.RecordDate, INTERVAL 1 DAY)
WHERE c.Temperature > p.Temperature