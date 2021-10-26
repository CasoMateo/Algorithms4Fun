class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        odds = []
        evens = []
        
        for num in nums: 
          if num % 2 == 0: 
            evens.append(num)
          
          else: 
            odds.append(num)

        cur = -1
        
        for i in range(len(nums)):
          
          if i % 2 == 0: 
            nums[i] = evens[cur]
            
          else: 
            nums[i] = odds[cur]
            cur -= 1
          
        return nums
          
