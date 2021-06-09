class Solution:
    def totalMoney(self, n: int) -> int:
          
        money = 1
        ref = 0
        
        for i in range(2, n + 1):
   
          if (i - 1) % 7 == 0:
            ref += 6
          
          money += i - ref
        
        return money
