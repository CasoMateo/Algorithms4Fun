**Algorithm Idea**

Binary search approach. If a number is greater than 1, it's square root will 
be less than less than its half. Thus, we can check i * i == n until n / 2. 

**Complexities**

Time: O(log(N)).
Space: O(1).

**Results**

Runtime: 36 ms, faster than 73.34% of Python3 online submissions for Sqrt(x).
Memory Usage: 14.1 MB, less than 89.63% of Python3 online submissions for Sqrt(x).
