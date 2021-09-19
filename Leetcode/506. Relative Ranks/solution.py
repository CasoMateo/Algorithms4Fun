class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
          
        mem = {}
        cur = 1
        
        for j in sorted(scores, reverse = True):
          mem[j] = cur
          cur += 1 
          
        mem_places = {'1': 'Gold Medal', '2': 'Silver Medal', '3': 'Bronze Medal'}
 
        for i in range(len(scores)):
          
          if str(mem[scores[i]]) in mem_places:
            scores[i] = mem_places[str(mem[scores[i]])]
          
          else: 
            scores[i] = str(mem[scores[i]])
            
        return scores
