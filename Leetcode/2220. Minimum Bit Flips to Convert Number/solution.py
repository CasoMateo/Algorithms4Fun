class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        bin1 = self.addZeroes(bin(start)[2: ], len(bin(goal)[2: ]))
        bin2 = self.addZeroes(bin(goal)[2: ], len(bin(start)[2: ]))
        
        flips = 0 
        
        for i in range(len(bin1)):
            if bin1[i] != bin2[i]: 
                flips += 1 
        
        return flips
    
    def addZeroes(self, rep, needed):
        
        cur = len(rep)
        rep = list(rep)
        
        while cur < needed: 
            rep = ['0'] + rep 
            cur += 1 
        
        return rep
