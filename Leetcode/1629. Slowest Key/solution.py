class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
      longest = releaseTimes[0]
      cur = keysPressed[0]
      
      for i in range(1, len(keysPressed)):
        if releaseTimes[i] - releaseTimes[i - 1] > longest: 
          longest = releaseTimes[i] - releaseTimes[i - 1]
          cur = keysPressed[i]
        
        elif releaseTimes[i] - releaseTimes[i - 1] == longest: 
          if ord(keysPressed[i]) > ord(cur):
             longest = releaseTimes[i] - releaseTimes[i - 1]
             cur = keysPressed[i]
        
      return cur
