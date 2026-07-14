class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        n = len(nums)

        @lru_cache(None)
        def dfs(i, g1, g2):
            if i == n:
                if g1 > 0 and g1 == g2:
                    return 1
                return 0

            x = nums[i]

            # Skip nums[i].
            ans = dfs(i + 1, g1, g2)

            # Put nums[i] into the first subsequence.
            ng1 = x if g1 == 0 else gcd(g1, x)
            ans += dfs(i + 1, ng1, g2)

            # Put nums[i] into the second subsequence.
            ng2 = x if g2 == 0 else gcd(g2, x)
            ans += dfs(i + 1, g1, ng2)

            return ans % MOD

        return dfs(0, 0, 0)