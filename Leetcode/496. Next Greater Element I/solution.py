class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
      
      elements = []
      
      for i in range(len(nums1)):
        found = False
        for j in range(nums2.index(nums1[i]), len(nums2)):
          
          if nums2[j] > nums1[i]: 
  
            found = True 
            elements.append(nums2[j])
            break
        
        if not found: 
          elements.append(-1)
      
      return elements
        
        
