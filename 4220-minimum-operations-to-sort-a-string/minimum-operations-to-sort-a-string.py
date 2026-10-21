class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # Already sorted
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0

        # Cannot sort the entire string in one operation
        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        # Minimum already at start or maximum at end
        if s[0] == mn or s[-1] == mx:
            return 1

        # Minimum or maximum exists in the middle
        for ch in s[1:-1]:
            if ch == mn or ch == mx:
                return 2

        return 3
