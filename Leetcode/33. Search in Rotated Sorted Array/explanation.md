**Algorithm Idea**

Get the original array by slicing the given one 
according the number of times it was shifted. Then, use the 
binary search algorithm to identify the index of the target 
value, if it exists. If such number was found, adjust the resulting 
index in a way that takes into account the original amount of times the 
array was shifted. 

**Complexities**

Time: O(log(N)).
Space: O(1).

**Results**

Runtime: 40 ms, faster than 73.17% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.5 MB, less than 80.63% of Python3 online submissions for Search in Rotated Sorted Array.
