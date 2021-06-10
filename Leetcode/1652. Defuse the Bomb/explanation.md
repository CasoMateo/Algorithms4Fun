**Algorithm Idea**

To get the sum of the k previous elements, 
add code[i - j], where i represents 
the iterator and j incorporates the k variable, for every item of the list. 
On the contrary, compute code[(i +  j) % len(code)], similarly, to find the 
sum of the k next
elements.

**Complexities**

Time: O(N * k).
Space: O(N) - output array.

**Results**

Runtime: 56 ms, faster than 31.05% of Python3 online submissions for Defuse the Bomb.
Memory Usage: 14.1 MB, less than 84.55% of Python3 online submissions for Defuse the Bomb.
