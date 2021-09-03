**Algorithm Idea**

Iterate over the list backwards, and 
keep a count of the current number of digits. 
If it exceeds three, place a dot before 
adding the current element. At the end, reverse 
the list and convert it into a string. The use of 
strings is avoided because of Python string 
immutability. 

**Complexities**

Time: O(N).
Space: O(N). - Python string immutability.

**Complexities**

Runtime: 23 ms, faster than 94.69% of Python3 online submissions for Thousand Separator.
Memory Usage: 14.2 MB, less than 75.37% of Python3 online submissions for Thousand Separator.
