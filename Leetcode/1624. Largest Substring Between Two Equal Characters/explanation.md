**Algorithm Idea**

For every item in the list, check if it has already been seen. 
If it has, then find the difference between the indexes in which 
they have been found. Update the maximum length based on the 
current count and the previous maximum count.

**Complexities**

Time: O(N).
Space: O(N).

**Results**

Runtime: 16 ms, faster than 84.43% of Python online submissions for Largest Substring Between Two Equal Characters.
Memory Usage: 13.4 MB, less than 88.52% of Python online submissions for Largest Substring Between Two Equal Characters.
