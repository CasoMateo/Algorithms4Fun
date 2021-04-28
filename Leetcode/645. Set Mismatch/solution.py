class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        have = set()
        required = set(range(1, len(nums) + 1))
        ans =[]
        for n in nums:
            if n in have:
                ans.append(n)
            else:
                have.add(n)
        
        ans.append(*(required - have)) 
        
        return ans
