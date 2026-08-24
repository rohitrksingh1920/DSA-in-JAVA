class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        total = sum(stones)
        best = total

        for i in range(len(stones) - 2, 0, -1):
            total -= stones[i + 1]
            best = max(best, total - best)

        return best