class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        arr = []
        for i, (start, end, weight) in enumerate(intervals):
            arr.append((start, end, weight, i))

        arr.sort(key=lambda x: x[1])

        # Find the last interval ending before start
        ends = [x[1] for x in arr]

        from bisect import bisect_left

        # dp[i][k] = (maximum weight, indices)
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            start, end, weight, idx = arr[i - 1]

            # Number of intervals before current one
            p = bisect_left(ends, start, 0, i - 1)

            for k in range(1, 5):

                # Option 1: skip current interval
                best = dp[i - 1][k]

                # Option 2: take current interval
                prevWeight, prevIndices = dp[p][k - 1]

                candidateWeight = prevWeight + weight
                candidateIndices = prevIndices + [idx]

                if candidateWeight > best[0]:
                    best = (candidateWeight, candidateIndices)

                elif candidateWeight == best[0]:
                    if sorted(candidateIndices) < sorted(best[1]):
                        best = (candidateWeight, candidateIndices)

                dp[i][k] = best

        return sorted(dp[n][4][1])