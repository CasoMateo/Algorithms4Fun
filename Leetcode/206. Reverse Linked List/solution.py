# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
      stack = []
      cur = head
      
      while cur != None:
        stack.append(cur.val)
        cur = cur.next

      ac = -1
      reverse = head
      
      while reverse != None:
        reverse.val = stack[ac]
        ac -= 1 
        reverse = reverse.next
        
      return head
