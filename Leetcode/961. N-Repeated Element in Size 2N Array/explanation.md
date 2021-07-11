**Algorithm Idea**

Solution 1: Denote the current item as negative. 
Later on, check if there are any 
negative elements with respect to the current one. 

Solution 2: Create a set to store elements. 
Through the iteration, check if the current item has 
already been seen. 

**Complexities**

Solution 1: 

Time: O(N²) - list look-up is linear.
Space: O(1).

Solution 2: 

Time: O(N).
Space: O(N).

**Results**

Solution: 

Runtime: 192 ms, faster than 95.23% of Python3 online submissions for N-Repeated Element in Size 2N Array.
Memory Usage: 15.6 MB, less than 75.85% of Python3 online submissions for N-Repeated Element in Size 2N Array.

Solution 2: 

Runtime: 196 ms, faster than 87.06% of Python3 online submissions for N-Repeated Element in Size 2N Array.
Memory Usage: 15.6 MB, less than 75.85% of Python3 online submissions for N-Repeated Element in Size 2N Array.


