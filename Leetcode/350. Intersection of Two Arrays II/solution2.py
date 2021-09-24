from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
      
      
      if len(nums1) > len(nums2):
        nums2, nums1 = nums1, nums2
        
      mem = Counter(nums2)
      intersection = []
      
      for i in range(len(nums1)):
        if nums1[i] in nums2:
          if mem[nums1[i]] > 0: 
            mem[nums1[i]] -= 1 
          
            intersection.append(nums1[i])
      
      return intersection
