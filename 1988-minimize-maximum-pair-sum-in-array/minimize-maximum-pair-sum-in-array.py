class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1

        maxSum = 0

        while left < right:
            maxSum = max(maxSum, nums[left] + nums[right])
            left += 1
            right -= 1

        return maxSum