class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = [nums[0]]
        
        for num in nums[1:]:
            if num > subsequence[-1]:
                sub.append(num)
            else:
                
                iterator = 0
                while num > subsequence[iterator]:
                    iterator += 1
                subsequence[iterator] = num

        return len(subsequence)
      
    
