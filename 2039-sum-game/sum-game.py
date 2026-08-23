class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        leftSum = 0
        rightSum = 0
        leftQ = 0
        rightQ = 0

        for i in range(half):
            if num[i] == '?':
                leftQ += 1
            else:
                leftSum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                rightQ += 1
            else:
                rightSum += int(num[i])

        diff = leftSum - rightSum
        qDiff = leftQ - rightQ

        if qDiff % 2 != 0:
            return True

        return diff != -9 * (qDiff // 2)