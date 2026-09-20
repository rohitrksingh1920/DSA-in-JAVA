class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):
            value = ord(s[i]) - ord('a') + 1
            reverseValue = 26 - value + 1
            ans += reverseValue * (i + 1)

        return ans