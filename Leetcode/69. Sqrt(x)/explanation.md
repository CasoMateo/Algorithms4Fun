**Algorithm Idea**

Binary search approach. If a number is greater than 1, it's square root will 
be less than less than its half. Thus, we can check i * i == n until n / 2. 

**Complexities**

Time: O(log(n))
Space: O(1)

**Results**

Runtime: 36 ms, faster than 57.43% of Python3 online submissions.
Memory Usage: 14.2 MB, less than 68.87% of Python3 online submissions. 
