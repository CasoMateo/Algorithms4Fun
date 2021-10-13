**Algorithm Idea**

If the current element has a greater value than the one before, 
remove such number from the accumulated sum, and, instead, replace 
it with the problem specifications in the prompt. Compute cur - last,
where cur is greater. Otherwise, increase the variable according to 
the current symbol's value.

**Complexities**

Time: O(N).
Space: O(1).

**Results**

Runtime: 46 ms, faster than 73.55% of Python3 online submissions for Roman to Integer.
Memory Usage: 14.3 MB, less than 57.86% of Python3 online submissions for Roman to Integer.

