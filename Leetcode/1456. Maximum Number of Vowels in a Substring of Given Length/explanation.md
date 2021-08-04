**Algorithm Idea**

Find the number of vowels in the 
first substring of length k. As 
the string is traversed from 1 to 
its length, check if the current 
character is a vowel. If so, 
increase the initial count by one. 
On the other hand, check if the first 
character of the last substring is a 
vowel, and decrease the count respectively. 
This way, we shift a substring of size k 
across the array to account for all possible 
combinations. 

**Complexities**

Time: O(N).
Space: O(1).

**Results**

Runtime: 148 ms, faster than 90.94% of Python3 online submissions for Maximum Number of Vowels in a Substring of Given Length.
Memory Usage: 14.8 MB, less than 75.67% of Python3 online submissions for Maximum Number of Vowels in a Substring of Given Length.
