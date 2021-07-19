class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
      
      count = 0 
      
      if ruleKey == 'type': 
        x = 0
      elif ruleKey == 'color': 
        x = 1 
      else: 
        x = 2
      
      for item in items: 
        if item[x] == ruleValue: 
          count += 1 
      
      return count
