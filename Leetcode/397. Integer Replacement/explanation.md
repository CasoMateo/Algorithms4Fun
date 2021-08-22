**Algorithm Idea**

Each iteration, replace the current form of the 
integer according to the problem constraints. When 
the digit is odd, optimize the operation by  
looking at future terms, and whether they would be even 
numbers. This is because even numbers are divided by two, 
making us reach the digit 1 more rapidly.

**Complexities**

Time: O(N).
Space: O(1).

**Results**

Runtime: 28 ms, faster than 88.47% of Python3 online submissions for Integer Replacement.
Memory Usage: 14 MB, less than 99.42% of Python3 online submissions for Integer Replacement.
