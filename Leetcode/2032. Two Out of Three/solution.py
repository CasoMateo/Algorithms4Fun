
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
      
      mem1 = set(nums1)
      mem2 = set(nums2)
      mem3 = set(nums3)
      
      arrs = [mem1, mem2, mem3]
      
      terms = set()
      
      for num in nums1: 
        terms.add(num)
      
      for num in nums2: 
        terms.add(num)
      
      for num in nums3: 
        terms.add(num)
      
      two = []
      
      for i in terms: 
        cur = 0 
        
        for j in range(len(arrs)):
          if i in arrs[j]:
            cur += 1 
        
        if cur >= 2: 
          two.append(i)
      
      return two
            
        
