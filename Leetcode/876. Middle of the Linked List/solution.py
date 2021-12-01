class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
      elements = []
      cur = head
      
      while cur != None:
        elements.append(cur)
        cur = cur.next
 
      return elements[len(elements) // 2]
      
