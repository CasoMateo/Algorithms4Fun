**Algorithm Idea**

Sort the list, and find the number of elements between  
the current number and that same digit plus one, if it exists. 
This way, we are assured of the fact that the difference 
between the maximum and minimum items in the sequence is equal 
to one. Update the longest variable based on the sequence's respective length. 

**Complexities**

Time: O(Nlog(N)).
Space: O(N).


**Results**

Runtime: 368 ms, faster than 34.76% of Python3 online submissions for Longest Harmonious Subsequence.
Memory Usage: 15.9 MB, less than 53.49% of Python3 online submissions for Longest Harmonious Subsequence.
