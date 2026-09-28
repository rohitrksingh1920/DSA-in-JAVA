class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxDepth = 0

        for ch in s:
            if ch == '(':
                count += 1
                maxDepth = max(maxDepth, count)

            elif ch == ')':
                count -= 1

        return maxDepth