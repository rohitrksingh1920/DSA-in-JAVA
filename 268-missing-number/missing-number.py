class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        actualSum = n * (n + 1) // 2
        currSum = 0

        for num in nums:
            currSum += num

        return actualSum - currSum
