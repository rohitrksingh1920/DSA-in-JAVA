class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def backTrack(curr, openCount, closeCount):
            if len(curr) == 2 * n:
                ans.append(curr)
                return

            if openCount < n:
                backTrack(curr + '(', openCount + 1, closeCount)

            if closeCount < openCount:
                backTrack(curr + ')', openCount, closeCount + 1)

        backTrack("", 0, 0)
        return ans