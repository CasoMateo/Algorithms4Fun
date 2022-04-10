class Solution:
    def largestInteger(self, num: int) -> int:
      num = list(str(num))
      
      for i in range(len(num)): 
        cur = second = 0
        for j in range(i + 1, len(num)): 
          if int(num[j]) % 2 == int(num[i]) % 2: 
            if int(num[j]) - int(num[i]) > cur: 
              cur = int(num[j]) - int(num[i])
              second = j
        
        if cur > 0: 
          num[i], num[second] = num[second], num[i]
      
      return int(''.join(num))
