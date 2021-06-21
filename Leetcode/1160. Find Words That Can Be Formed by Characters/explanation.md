**Algorithm Idea**

For every string in the list, check if every 
character is to be found in chars. If it is 
present, remove the character from a temporary 
copy of chars, which is created each 
iteration.

**Complexities**

Time: O(N²) - where N is the the length of the list.
Space: O(M) - where M is the length of chars.

**Results**

Runtime: 96 ms, faster than 84.24% of Python3 online submissions for Find Words That Can Be Formed by Characters.
Memory Usage: 14.5 MB, less than 91.90% of Python3 online submissions for Find Words That Can Be Formed by Characters.
