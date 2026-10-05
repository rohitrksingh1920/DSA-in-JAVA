class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # n = len(s)

        # return n // 2


        scr = 0
        depth = 0

        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1

                if s[i - 1] == '(':
                    scr += 2 ** depth

        return scr