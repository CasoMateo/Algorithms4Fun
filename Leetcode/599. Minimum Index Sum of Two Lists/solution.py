class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        mem = {}
        
        for i in range(len(list2)):
          mem[list2[i]] = i 
        
        least = []
        cur = float('inf')
        
        for j in range(len(list1)):
          if list1[j] in mem: 
            if mem[list1[j]] + j < cur:
              least = []
              least.append(list1[j])
              cur = mem[list1[j]] + j
            
            elif mem[list1[j]] + j == cur: 
              least.append(list1[j])
              
        return least
