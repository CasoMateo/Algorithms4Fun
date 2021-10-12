**Algorithm Idea**

Loop through all balls (lowLimit, highLimit), 
and get the current sum of digits each iteration. 
If the such combination has already been seen, 
increment its respective frequency in the dictionary. 
Traverse the hash table and find the ball with the 
highest frequency. 

**Complexities**

Time: O(N * m) - where m is the length of highLimit.
Space: O(N).

**Results**

Runtime: 628 ms, faster than 52.09% of Python3 online submissions for Maximum Number of Balls in a Box.
Memory Usage: 14.1 MB, less than 81.96% of Python3 online submissions for Maximum Number of Balls in a Box.
