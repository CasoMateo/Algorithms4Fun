class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        used = defaultdict(int)
        pairs = 0
        
        for num in nums:
            pairs += used[num - k] + used[num + k]
            used[num] += 1
            
        return pairs
