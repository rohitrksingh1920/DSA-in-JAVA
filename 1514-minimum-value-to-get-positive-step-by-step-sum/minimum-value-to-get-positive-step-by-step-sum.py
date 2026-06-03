class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        curSum = 0
        minSum = float('inf')

        for num in nums:
            curSum += num
            minSum = min(minSum, curSum)

        return max(1, 1 - minSum)