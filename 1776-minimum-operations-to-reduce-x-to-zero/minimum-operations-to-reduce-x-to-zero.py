class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x

        if target < 0:
            return -1

        left = 0
        currSum = 0
        maxLen = -1

        for right in range(len(nums)):
            currSum += nums[right]

            while currSum > target:
                currSum -= nums[left]
                left += 1

            if currSum == target:
                maxLen = max(maxLen, right - left + 1)

        if maxLen == -1:
            return -1

        return len(nums) - maxLen