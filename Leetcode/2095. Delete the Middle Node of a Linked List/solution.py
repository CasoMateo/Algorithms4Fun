
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
      length = 0 
      
      cur = head 
      
      while cur: 
        length += 1 
        cur = cur.next 
      
      length //= 2 
  
      ac = 0 
      cur = head 
      
      if length == 0:
        return
      
      while True: 
        ac += 1 
        
        if ac == length: 
          cur.next = cur.next.next 
          break 
        
        else:
          cur = cur.next
          
      return head
        
        
      
