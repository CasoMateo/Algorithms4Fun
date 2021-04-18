**Algorithm Idea**

Initialize two pointers, low and high, pointing to the first and last indexes of the array. 
While low is less than or equal to high, compute a mid variable, which is equal to low + high 
over two. This operation will constantly divide the array by two. Then, check whether arr[mid] is 
less than the target, if it is, than adjust lo to mid + 1. In the opposite case, set high to 
mid - 1. Otherwise, return the index at which the target was found. 

**Complexities**
Time: O(len(n)).
Space: O(1).

**Results**
Runtime: 228 ms, faster than 90.92% of Python3 online submissions.
Memory Usage: 15.5 MB, less than 90.31% of Python3 online submissions

