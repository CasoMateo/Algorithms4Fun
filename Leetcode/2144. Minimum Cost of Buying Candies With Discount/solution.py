class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        
        cost.sort()
        cost = cost[:: -1]
        
        ac = sum(cost)
        cur = 0 
        
        if len(cost) <= 2: 
            return ac
        
        for i in range(len(cost)):
            if cur == 2:
                ac -= cost[i]
            
            cur += 1
            
            if cur == 3:
                cur = 0
        
        return ac
                
                
