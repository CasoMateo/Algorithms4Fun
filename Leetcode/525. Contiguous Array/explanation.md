**Algorithm Idea**

Keep a count of the current substring, stating whether it has an equal 
count of zeroes and ones. If it isn't, look for a substring within the greater 
string that has the same "charge". Remove it from the current string to get 
a contiguous array. 

**Complexities**

Time: O(N).
Space: O(N).

**Results**

Runtime: 1046 ms, faster than 65.65% of Python3 online submissions for Contiguous Array.
Memory Usage: 19.3 MB, less than 80.26% of Python3 online submissions for Contiguous Array.
