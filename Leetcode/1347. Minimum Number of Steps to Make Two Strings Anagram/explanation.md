**Algorithm Idea**

Find the character frequencies in both t and s. 
Iterate over the "t" frequency dictionary and 
look for the following cases: 

- DictionaryT[char] > DictionaryS[char]: 
Do DictionaryT[char] - DictionaryS[char] operations. 

- DictionaryT[char] not in DictionaryS: 
Do DictionaryT[char] operations. 

**Complexities**

Time: O(N).
Space: O(N).

**Results**

Runtime: 116 ms, faster than 75.96% of Python3 online submissions for Minimum Number of Steps to Make Two Strings Anagram.
Memory Usage: 14.7 MB, less than 85.67% of Python3 online submissions for Minimum Number of Steps to Make Two Strings Anagram.
