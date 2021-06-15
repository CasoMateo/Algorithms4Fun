**Algorithm Idea**
Look for each letter of the first word in the 
rest of the input's items. Denote a variable 
common as False if the letter is not to be found, 
and if it is present, remove one occurrence of the 
character in the string.

**Complexities**

Time: O(N*M) - where N is the length of the list and M is the number 
of characters within the subarray. 

Space: O(M) - output array. 

**Results**

Runtime: 60 ms, faster than 32.47% of Python3 online submissions for Find Common Characters.
Memory Usage: 14.2 MB, less than 94.33% of Python3 online submissions for Find Common Characters.
