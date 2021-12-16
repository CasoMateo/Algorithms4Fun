# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0    self.next = next
class Solution:
  def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
  
    vals = []
  
    cur = head 

    while cur: 
      vals.append(cur.val)
      cur = cur.next

    vals.sort()

    cur = head 
    ac = 0
    
    while cur: 
      cur.val = vals[ac]
      ac += 1 
      cur = cur.next 

    return head
