**Algorithm Idea**

For every two rungs, compute the difference between 
the current one and the previous one. If the difference 
is greater than dist, account for the number of times 
one would need to add a rung in order to make the difference
less than or equal to dist. This can be done by finding the 
number of times dist fits into such difference.

**Complexities**

Time: O(N).
Space: O(1).

**Results**

Runtime: 528 ms, faster than 50.00% of Python3 online submissions for Add Minimum Number of Rungs.
Memory Usage: 29 MB, less than 50.00% of Python3 online submissions for Add Minimum Number of Rungs.
