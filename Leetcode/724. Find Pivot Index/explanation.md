**Algorithm Idea**

Keep track of the current sum (sum to the left), 
and check whether the left and right sums are 
equal for each iteration. The right sum is computed by 
substracting the current sum and the current item from 
the total sum. 

**Complexities**

Time: O(N).
Space: O(1).

**Results**

Runtime: 144 ms, faster than 86.84% of Python3 online submissions for Find Pivot Index.
Memory Usage: 15.2 MB, less than 99.14% of Python3 online submissions for Find Pivot Index.
