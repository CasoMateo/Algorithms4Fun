**Algorithm Idea**
Initialize a memo structure and denote the first and second indexes to be 1 and 2 respectively. Use 
a for loop to add the solutions to the 2 previous indexes, until the value of memo[n] is computed. 

**Complexities** 
Time: O(n) - one for loop is used. 
Space: O(n) - one array of the size of the input is used.

**Results**
Runtime: 32 ms, faster than 44.86% of Python3 online submissions.
Memory Usage: 13.9 MB, less than 98.01% of Python3 online submissions for Climbing Stairs.
