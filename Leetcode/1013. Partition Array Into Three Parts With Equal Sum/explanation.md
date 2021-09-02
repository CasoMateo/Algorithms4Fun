**Algorithm Idea**

If any three subarrays have the same sum, each 
subarray will be a third of the total one. Iterate 
over the array and keep a sum of the current elements. 
Check if the sum that corresponds to each subarray has 
already been met, and if so, increase the count of found 
sublists. 

**Complexities**

Time: O(N).
Space: O(1).

**Results**

Runtime: 342 ms, faster than 28.05% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
Memory Usage: 20.9 MB, less than 94.91% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
