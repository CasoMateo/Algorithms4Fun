class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
      
      seats.sort()
      students.sort()
      
      operations = 0 
      
      for i in range(len(seats)):
        operations += abs(seats[i] - students[i])
      
      return operations
        
