**Algorithm Idea** 

Create an array the size of n with "True" values. As the list is iterated and mem[i] is 
True, the number of solutions is increased. Denote all multiples of mem[i] "False". 
Repeat the same process. 

**Complexities**

Time: O(N²)
Space: O(N)

**Results**

Time: 552 ms, faster than 66.58% of Python3 online submissions. 
Space: 25.6 MB, less than 75.63% of Python3 online submissions.
