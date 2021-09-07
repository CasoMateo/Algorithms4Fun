**Algorithm Idea**

Use the idea that that you can get 
all divisors of a number by iterating 
up to its square root. If the current 
number evenly divides the input, 
add the integer to a set that is reset 
every iteration and check if 
the length of such hash table equals 4. 
If it does, add the sum of the set to the 
result. This works because the numbers that 
are not located before the square root of the 
number can be found by using the results
of even divisions. 

**Complexities**

Time: O(N²).
Space: O(N).

**Results**

Runtime: 352 ms, faster than 92.20% of Python3 online submissions for Four Divisors.
Memory Usage: 15.4 MB, less than 77.31% of Python3 online submissions for Four Divisors.
