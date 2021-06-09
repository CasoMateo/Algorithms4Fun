class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
      av = 0
      
      if len(flowerbed) == 1:
        if flowerbed[0] == 0 and n < 2: 
          return True 
        elif flowerbed[0] == 1 and n == 0: 
          return True 
        return False
      
      for i in range(len(flowerbed)):
        if i == 0 and flowerbed[i] == 0: 
          if flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            av += 1
            continue
        if i == len(flowerbed) - 1 and flowerbed[i] == 0:
          if flowerbed[i - 1] == 0:
            flowerbed[i] = 1
            av += 1

        if flowerbed[i] == 1:
          continue
        if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
          flowerbed[i] = 1
          av += 1 

      if av >= n: 
        return True 
      return False
          
