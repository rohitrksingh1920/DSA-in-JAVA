class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        n = len(word)

        for i in range(n):
            ans += i // 8 + 1

        return ans
