class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
      
      mem = {}
      
      for num in nums: 
        mem[num] = mem.get(num, 0) + 1
      
      frequencies = {}
      
      for freq in mem: 
        if mem[freq] in frequencies:
          frequencies[mem[freq]].append(freq)
        
        else:
          frequencies[mem[freq]] = [freq]
    
      increasing = []
      frequencies = dict(sorted(frequencies.items()))
      
      for prior in frequencies:
        frequencies[prior] = sorted(frequencies[prior], reverse = True)
        for num in frequencies[prior]:
          increasing.extend([num] * mem[num])
        
      return increasing
        
