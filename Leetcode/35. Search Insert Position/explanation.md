**Algorithm Idea**

Compute a binary search on the array. If the element wasn't found, 
loop through the array and look for an item such that it is smaller 
than the target, and the target is smaller than the next element. 
If this condition wasn't met, then either return 0 or the length of the 
array depending on the minimum value.

**Complexities**

Time: O(N + log(N)) = O(N).
Space: O(1).

**Results**

Runtime: 44 ms, faster than 89.22% of Python3 online submissions.
Memory Usage: 15 MB, less than 79.53% of Python3 online submissions.
