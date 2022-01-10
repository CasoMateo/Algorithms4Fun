class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
      
      nums = []
      
      cur = head 
      
      while cur: 
        nums.append(cur.val)
        cur = cur.next
      
      largest = 0
      for i in range(len(nums)):
        cur = nums[i] + nums[len(nums) - i - 1]
        largest = max(largest, cur)
      
      return largest
