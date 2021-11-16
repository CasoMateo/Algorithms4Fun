class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
      seen = set()
      cur = head
      
      if not cur: 
        return False
      
      while cur.next != None: 
        
        if cur in seen: 
          return True 
        
        seen.add(cur)
        cur = cur.next
      
      return False
