class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')

        best = [INF] * (n + 1)

        left = 0
        currSum = 0
        answer = INF

        for right in range(n):
            currSum += arr[right]

            while currSum > target:
                currSum -= arr[left]
                left += 1

            if currSum == target:
                length = right - left + 1

                if best[left] != INF:
                    answer = min(answer, length + best[left])

                best[right + 1] = min(best[right], length)
            else:
                best[right + 1] = best[right]

        return -1 if answer == INF else answer