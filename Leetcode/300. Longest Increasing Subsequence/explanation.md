**Algorithm Idea**

For each item, check if it is greater 
than the last number in the subsequence. 
If so, append it to the list, which will
later be returned. On the contrary, look 
for the first element in the subsequence 
that is greater than or equal to the 
current element. Replace the previous 
value with the current one. 


**Complexities*+

Time: O(N²).
Space: O(N).

**Results**

Runtime: 128 ms, faster than 71.70% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 14.5 MB, less than 74.98% of Python3 online submissions for Longest Increasing Subsequence.
