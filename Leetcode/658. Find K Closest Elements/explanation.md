**Algorithm Idea**

Create an array where each element is sorted based 
on its respective difference with regard to x. 
Then, iterate through this structurue k number of 
times. 

**Complexities**

Time: O(Nlog(N)) - we also sort the output array (Klog(K)), but the length of the array 
will always be larger than k.
Space: O(N).

**Results**

Runtime: 304 ms, faster than 57.88% of Python3 online submissions for Find K Closest Elements.
Memory Usage: 15.6 MB, less than 70.58% of Python3 online submissions for Find K Closest Elements.
