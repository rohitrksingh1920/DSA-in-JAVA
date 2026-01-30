class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        actual_sum = n * (n + 1) // 2
        curr_sum = 0

        for num in nums:
            curr_sum += num

        return actual_sum - curr_sum
