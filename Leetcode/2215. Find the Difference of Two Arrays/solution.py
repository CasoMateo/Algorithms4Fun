class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        mem1 = set(nums1)
        mem2 = set(nums2)
        
        answer = [-1, -1] 
        
        answer[0] = self.individualDifference(mem1, mem2)
        answer[1] = self.individualDifference(mem2, mem1)
        
        return answer   
    
    def individualDifference(self, nums1, nums2):
        cur = []
        for num in nums1: 
            if num not in nums2: 
                cur.append(num)
        
        return cur
                
