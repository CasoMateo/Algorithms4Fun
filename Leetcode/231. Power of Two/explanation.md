**Algorithm Idea**

Divide the number by 2 until the current quantity modulo 2 is not 0. 
In which case, return False. If the condition was never met, the 
input is, in fact, a power of 2. 

**Complexities** 

Time: O(log(N)). 
Space: O(1).

**Results**

Runtime: 24 ms, faster than 96.24% of Python3 online submissions.
Memory Usage: 14.2 MB, less than 69.35% of Python3 online submissions.
