class Solution:
    def reformatNumber(self, number: str) -> str:
      
      digits = []
      
      for i in range(len(number)):
        if number[i].isdigit():
          digits.append(number[i])
      
      reformatted = []
      
      while len(digits) > 0:
        if len(digits) > 4:
          reformatted.append(digits[: 3])
          digits = digits[3: ]
        
        elif len(digits) == 4:
          reformatted.append(digits[: 2])
          reformatted.append(digits[2: ])
          digits = []
        
        else:
          reformatted.append(digits)
          digits = []
      
      final = ''
      
      for each in range(len(reformatted) - 1):
        final += ''.join(reformatted[each]) + '-'
      
      final += ''.join(reformatted[-1])
      return final
