**Algorithm Idea**
Get the array's max and min values, and while iterating, check whether the current element is 
not equal to both values. If it is not, then add the salaries[i] to a sum variable. At the 
end, divide sum by len(salaries) - 2.

**Complexities**
Time: O(n) - one for loop.
Space: O(1). 

**Results**
Runtime: 24 ms, faster than 94.67% of Python3 online submissions.
Memory Usage: 14.2 MB, less than 71.38% of Python3 online submissions
