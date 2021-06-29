**Algorithm Idea**

Solution 1: Find the frequency of each element in both s, 
and compare the occurrences with t respectively. 
If an element within t is not found in s, 
return such item. 

Solution 2: Sort both arrays and find mismatching 
items.

**Complexities**

Solution 1: 

Time: O(N).
Space: O(N).

Solution 2: 

Time: O(Nlog(N)).
Space: O(N).

**Results**

Solution 1: 

Runtime: 36 ms, faster than 58.91% of Python3 online submissions for Find the Difference.
Memory Usage: 14.2 MB, less than 83.31% of Python3 online submissions for Find the Difference.

Solution 2: 

Runtime: 28 ms, faster than 94.48% of Python3 online submissions for Find the Difference.
Memory Usage: 14.3 MB, less than 59.56% of Python3 online submissions for Find the Difference.
