
class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        e = 0
        for n in chips:
            if n % 2 == 0:
                e += 1

        return min(e, len(chips) - e)
