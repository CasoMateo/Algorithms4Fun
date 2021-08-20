class Solution:
    def sortSentence(self, s: str) -> str:
      
        mem = {}
        
        for i in s.split():
            mem[i[-1]] = i[: -1]

        return ' '.join(mem[p] for p in sorted(mem))
