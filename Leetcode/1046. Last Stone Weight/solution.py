class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1: 
          cur1 = max(stones)
          im = stones.copy()
          im.remove(cur1)
          cur2 = max(im)
          
          if cur1 == cur2: 
            stones.remove(cur1)
            stones.remove(cur2)
          
          else: 
            for i in range(len(stones)):
              if stones[i] == cur1: 
                stones[i] = cur1 - cur2 
                break
                
            stones.remove(cur2)
          
        return stones[0] if stones else 0
            
