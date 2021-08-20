**Algorithm Idea**

Compute the sum of the initial k elements in 
the list. Then, add and substract external elements 
correspondingly to slide a k-sized subarray over 
the list (sliding window). Update a "longest" variable 
in order to store the greatest average subarray of length k 
by comparing the current sum. 

**Complexities**

Time: O(N).
Space: O(1).

**Results**

Runtime: 1156 ms, faster than 92.59% of Python3 online submissions for Maximum Average Subarray I.
Memory Usage: 25.8 MB, less than 68.20% of Python3 online submissions for Maximum Average Subarray I.
