**Algorithm Idea**

Start off with the first letter 
being the slowest, and update the current 
slowest character as we traverse the array. 
Check if the duration of the current letter 
is greater than the previous one, and if so, 
update the corresponding variables. In the case 
that both variables have the same duration, check 
which one is lexographically greater through the 
ord function. 

**Complexities**

Time: O(N).
Space: O(1).

**Results**

Runtime: 56 ms, faster than 77.56% of Python3 online submissions for Slowest Key.
Memory Usage: 14.3 MB, less than 93.84% of Python3 online submissions for Slowest Key.
