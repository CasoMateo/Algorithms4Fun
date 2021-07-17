class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      
      memreversed = {}
      product = 1
      
      for i in range(1, len(nums)):
        memreversed[len(nums) - i] = product * nums[len(nums) - i] 
        product *= nums[len(nums) - i]
  
      products = []
      product = 1 
      
      for j in range(len(nums)):
        
        if j == len(nums) - 1: 
          products.append(product)
          break
        
        products.append(product * memreversed[j + 1])
        product *= nums[j]
      
      return products
    
      
      
