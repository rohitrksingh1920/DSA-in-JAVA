class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        BASE = 911382323
        MOD1 = 1000000007
        MOD2 = 1000000009

        def check(k):
            h1 = h2 = 0

            for i in range(k):
                h1 = (h1 * BASE + nums[i]) % MOD1
                h2 = (h2 * BASE + nums[i]) % MOD2

            p1 = pow(BASE, k - 1, MOD1)
            p2 = pow(BASE, k - 1, MOD2)

            freq = {}

            for i in range(n - k + 1):
                key = h1 * MOD2 + h2
                freq[key] = freq.get(key, 0) + 1

                if i + k < n:
                    h1 = ((h1 - nums[i] * p1) * BASE
                          + nums[i + k]) % MOD1

                    h2 = ((h2 - nums[i] * p2) * BASE
                          + nums[i + k]) % MOD2

            return any(v == 1 for v in freq.values())

        left, right = 1, n
        ans = n

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
