class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefixSum = nums[0]

        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            prefixSum += nums[i]
            i += 1

        s = set(nums)

        while prefixSum in s:
            prefixSum += 1

        return prefixSum