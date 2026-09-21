class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            newDp = [0] * k

            newDp[num % k] += 1

            for r in range(k):
                newR = (r * num) % k
                newDp[newR] += dp[r]

            dp = newDp

            for r in range(k):
                ans[r] += dp[r]

        return ans