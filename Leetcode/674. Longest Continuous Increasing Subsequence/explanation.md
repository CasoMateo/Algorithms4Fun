**Algorithm Idea** 

Use two variables, longest and cur, to keep track of the maximum number of times the array has been increasing. For each iteration, check if the previous 
element is less than the current one, and if this is the case, increase the variable cur. Then, select the maximum variable for longest out of itself and 
cur. If the array decreases, start a new count for cur.

**Complexitites** 

Time = O(n) 
Space = O(1) 

**Results** 

Runtime: 64 ms, faster than 98.15% of online Python 3 submissions. 
Memory Usage: 15.3 MB, less than 85.39 of online Python 3 submissions.

