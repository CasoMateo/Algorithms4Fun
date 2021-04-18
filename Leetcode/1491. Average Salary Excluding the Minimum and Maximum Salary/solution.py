class Solution:
    def average(self, salary: List[int]) -> float:
        min_ = min(salary)
        max_ = max(salary) 
        sum_ = 0
        
        for i in range(len(salary)): 
            if salary[i] != min_ and salary[i] != max_:
                sum_ += salary[i] 
                
        return sum_ / (len(salary) - 2) 
