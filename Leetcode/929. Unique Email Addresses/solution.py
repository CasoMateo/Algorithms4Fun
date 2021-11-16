class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
      mem = set()
      
      for i in range(len(emails)):
        cur = emails[i].split('@')
        local = ''
        
        for l in cur[0]:
          if l == '+':
            break
          
          elif l != '.':
            local += l
        
        mem.add(cur[1] + local)
            
      return len(mem)
