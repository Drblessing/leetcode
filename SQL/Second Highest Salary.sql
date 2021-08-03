# Write your MySQL query statement below
SELECT
(select distinct Salary as SecondHighestSalary
from Employee
order by Salary desc
limit 1 offset 1) as SecondHighestSalary;