class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
      
      elements = []
      cur = head
      
      while cur != None: 
        elements.append(cur.val)
        cur = cur.next
      
      return elements == elements[:: -1]
