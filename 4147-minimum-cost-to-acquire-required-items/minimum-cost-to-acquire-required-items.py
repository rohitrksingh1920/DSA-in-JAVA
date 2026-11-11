class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        
        if cost1 + cost2 <= costBoth:
            return need1*cost1 + need2*cost2

        both = min(need1, need2)
        total = both * costBoth

        need1 -= both
        need2 -= both

        if need1 > 0:
            total += need1 * min(cost1, costBoth)
        else:
            total += need2 * min(cost2, costBoth)

        return total
