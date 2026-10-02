class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []

        def backTrack(curr, openCount, closeCount):
            if len(curr) == 2 * n:
                stack.append(curr)
                return

            if openCount < n:
                backTrack(curr + '(', openCount + 1, closeCount)

            if closeCount < openCount:
                backTrack(curr + ')', openCount, closeCount + 1)

        backTrack("", 0, 0)
        return stack