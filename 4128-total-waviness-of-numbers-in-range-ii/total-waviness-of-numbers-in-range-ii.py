class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            @lru_cache(None)
            def dp(pos, tight, started, prev1, prev2):
                if pos == m:
                    return (1, 0)  # (count_numbers, total_waviness)

                limit = digits[pos] if tight else 9

                total_cnt = 0
                total_wave = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started:
                        if d == 0:
                            cnt, wav = dp(pos + 1, ntight, False, -1, -1)
                        else:
                            cnt, wav = dp(pos + 1, ntight, True, d, -1)

                        total_cnt += cnt
                        total_wave += wav
                        continue

                    add = 0

                    # prev2, prev1, d forms a triple
                    if prev2 != -1:
                        if (prev1 > prev2 and prev1 > d) or (
                            prev1 < prev2 and prev1 < d
                        ):
                            add = 1

                    cnt, wav = dp(pos + 1, ntight, True, d, prev1)

                    total_cnt += cnt
                    total_wave += wav + add * cnt

                return (total_cnt, total_wave)

            return dp(0, True, False, -1, -1)[1]

        return solve(num2) - solve(num1 - 1)