class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
      
      cur = head
      seen = 0
      
      if not cur:
        return False
      
      while cur.next != None:
        seen += 1
        
        if seen > 10000:
          return True
        
        cur = cur.next 
      
      return False
