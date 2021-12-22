# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
      
      nums = []
      cur = head 
      
      while cur: 
        nums.append(cur.val)
        cur = cur.next

      position = True
      cur = head 
      first = 0 
      last = -1
      
      while cur: 
        if position: 
          cur.val = nums[first]
          first += 1
          position = False 
        
        else: 
          cur.val = nums[last]
          last -= 1 
          position = True 
        
        cur = cur.next
