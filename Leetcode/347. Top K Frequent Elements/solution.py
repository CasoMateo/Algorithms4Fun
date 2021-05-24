from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        
        ans = []
        frequencies = Counter(nums)
        
        oc = sorted(frequencies, key = frequencies.get)
        
        for i in range(k):
            ans.append(oc.pop())
            
        return ans
