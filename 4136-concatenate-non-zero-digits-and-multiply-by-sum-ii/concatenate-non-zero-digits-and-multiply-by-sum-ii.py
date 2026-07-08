class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        prefSum = [0] * (n + 1)
        prefCnt = [0] * (n + 1)
        prefNum = [0] * (n + 1)

        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        for i, ch in enumerate(s):
            d = ord(ch) - ord('0')

            prefSum[i + 1] = prefSum[i]
            prefCnt[i + 1] = prefCnt[i]
            prefNum[i + 1] = prefNum[i]

            if d != 0:
                prefSum[i + 1] += d
                prefCnt[i + 1] += 1
                prefNum[i + 1] = (prefNum[i] * 10 + d) % MOD

        ans = []

        for l, r in queries:
            cnt = prefCnt[r + 1] - prefCnt[l]
            digitSum = prefSum[r + 1] - prefSum[l]

            x = (prefNum[r + 1] -
                 prefNum[l] * pow10[cnt]) % MOD

            ans.append((x * digitSum) % MOD)

        return ans