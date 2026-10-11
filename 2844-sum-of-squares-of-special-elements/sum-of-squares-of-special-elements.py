class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        length = n
        sum = 0
        for i in range(1, n + 1):
            if length % i == 0:
                sum += nums[i - 1] ** 2

        return sum