**ALGORITHM IDEA** 

Because the array is sorted, we can keep two pointers i and j. If nums[i] == nums[j], j is incremented. Otherwise, the value will be copied to nums[i + 1],
i is incremented and the process continues until the interation is finished.

**Complexities**
Time = O(n) 
Space = O(1) (in-place algorithm) 

**Results** 
Runtime: 80 ms, faster than 79.85% of Python 3 online submissions.
Memory usage: 15.8 MB, less than 51.71% of Python 3 online submissions.
