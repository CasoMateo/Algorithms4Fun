class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        output = []
        if k > 0: 
          for i in range(len(code)):
            cur = 0 
            for j in range(1, k + 1):
              cur += code[(i + j) % len(code)]
            output.append(cur)
              
        elif k < 0: 
          for i in range(len(code)):
            cur = 0 
            for j in range(1, abs(k) + 1):
              cur += code[i - j]
            output.append(cur)
        else: 
          for i in range(len(code)):
            output.append(0)
    
        return output 
