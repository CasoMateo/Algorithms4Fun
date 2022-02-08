    def minimumSum(self, num: int) -> int:
        digits = []
        
        for digit in str(num):
            digits.append(int(digit))
 
        digits.sort()
    
        return int(str(digits[0]) + str(digits[2])) + int(str(digits[1]) + str(digits[3]))
