class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = cur = 0
        
        for num in nums:
            if num == 1:
                cur += 1
                longest = max(longest, cur)
            else:
                cur = 0
        return longest
