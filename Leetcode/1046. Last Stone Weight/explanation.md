**Algorithm Idea**

Get the two greatest elements in stones, and 
check for the following cases:

- They are equal: remove both of them.
- They are not equal: get the index of the greatest item
and replace it with the difference between both elements.

Repeat this process until the length of the array becomes 
less than 2.

**Complexities**

Time: O(N²).
Space: O(N).

**Results**

Runtime: 28 ms, faster than 90.61% of Python3 online submissions for Last Stone Weight.
Memory Usage: 14.2 MB, less than 50.62% of Python3 online submissions for Last Stone Weight.
