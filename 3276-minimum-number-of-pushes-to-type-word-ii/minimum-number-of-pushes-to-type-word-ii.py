class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)

        counts = sorted(freq.values(), reverse=True)

        ans = 0

        for i, f in enumerate(counts):
            ans += (i // 8 + 1) * f

        return ans