**Algorithm Idea**

Find the original, sorted, version of the array. 
For every iteration, slice the list such that ith 
last elements are moved forward; then, check whether both arrays 
are equal.

**Complexities**

Time: O(Nlog(N)).
Space: O(N).

**Results**

Runtime: 32 ms, faster than 83.02% of Python3 online submissions for Check if Array Is Sorted and Rotated.
Memory Usage: 14.2 MB, less than 72.64% of Python3 online submissions for Check if Array Is Sorted and Rotated.

