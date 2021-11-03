**Algorithm Idea**

Get the order of each character in order 
through a hash table. Then, iterate over each 
character in the words and check for the following 
cases:

- Previous element is lexographically greater: return False 
- Previous element is lexographically equal: not strictly increasing

**Complexities**

Time: O(M) - where M is the number of characters.
Complexities: O(1).

**Results**

Runtime: 28 ms, faster than 97.21% of Python3 online submissions for Verifying an Alien Dictionary.
Memory Usage: 14.3 MB, less than 74.31% of Python3 online submissions for Verifying an Alien Dictionary.
