class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()

        dp = {}

        for num in nums:

            # Increase the current number by 1
            if num in dp:
                dp[num + 1] = dp[num] + 1
            else:
                dp[num + 1] = 1

            # Keep the current number unchanged
            if num - 1 in dp:
                dp[num] = dp[num - 1] + 1
            else:
                dp[num] = 1

        return max(dp.values())
