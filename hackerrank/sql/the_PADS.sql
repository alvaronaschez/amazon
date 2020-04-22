--https://www.hackerrank.com/challenges/the-pads/problem
-- using ms sql server syntax

select name + "(" + SUBSTRING(occupation, 1, 1) + ")" 
from occupations
order by name;

select "There are a total of " + CAST(count(*) as CHAR) + " " + lower(occupation) + "s."
from occupations
group by occupation
order by count(*);