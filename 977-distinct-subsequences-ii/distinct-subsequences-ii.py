class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = 1
        last = {}

        for char in s:
            new_dp = dp * 2

            if char in last:
                new_dp -= last[char]

            last[char] = dp
            dp = new_dp % MOD

        return (dp - 1) % MOD