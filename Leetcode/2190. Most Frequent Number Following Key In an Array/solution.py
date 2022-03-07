class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        
        mem = {}
        
        for i in range(len(nums) - 1): 
            if nums[i] == key: 
                mem[nums[i + 1]] = mem.get(nums[i + 1], 0) + 1
        
        maximum = 0 
        token = -1

        for freq in mem: 
            if mem[freq] > maximum: 
                maximum = mem[freq]
                token = freq
        
        return token
