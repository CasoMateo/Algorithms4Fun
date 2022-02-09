
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        pairs = set()
        mem = {}
        
        for num in nums: 
            mem[num] = mem.get(num, 0) + 1
            
        for i in range(len(nums)): 
            curLess = nums[i] - k 
            curMore = nums[i] + k 
        
            if curLess in mem: 
                if k == 0: 
                    if mem[nums[i]] <= 1:
                        continue 
                        
                pairs.add(str(curLess) + ' ' + str(nums[i]))
                
            if curMore in mem:
                pairs.add(str(nums[i]) + ' ' + str(curMore))
            
        return len(pairs)
