# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        number1 = self.getDigits(l1)
        number2 = self.getDigits(l2)
        
        added = str(int(number1) + int(number2))[:: -1]
        
        new = ListNode(101)
        ac = new
        actual = 0
        
        while actual <= len(added) - 1: 
            ac.next = ListNode(added[actual])
            ac = ac.next
            actual += 1 
            
  
        return new.next
    
    def getDigits(self, head): 
        cur = head 
        digits = ''
        
        while cur: 
            digits += str(cur.val)
            cur = cur.next 
        
        return digits[:: -1]
