class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo = {}

        def solve(rem):
            if rem == 0:
                return False

            if rem in memo:
                return memo[rem]

            i = 1
            while i * i <= rem:
                if not solve(rem - i * i):
                    memo[rem] = True
                    return True
                i += 1

            memo[rem] = False
            return False

        return solve(n)