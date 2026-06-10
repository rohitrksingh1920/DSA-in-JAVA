class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1

        m = lg[n] + 1

        mx = [[0] * n for _ in range(m)]
        mn = [[0] * n for _ in range(m)]

        for i in range(n):
            mx[0][i] = nums[i]
            mn[0][i] = nums[i]

        j = 1
        while (1 << j) <= n:
            half = 1 << (j - 1)
            limit = n - (1 << j) + 1

            for i in range(limit):
                mx[j][i] = max(mx[j - 1][i],
                               mx[j - 1][i + half])
                mn[j][i] = min(mn[j - 1][i],
                               mn[j - 1][i + half])
            j += 1

        def value(l, r):
            p = lg[r - l + 1]
            mxv = max(mx[p][l], mx[p][r - (1 << p) + 1])
            mnv = min(mn[p][l], mn[p][r - (1 << p) + 1])
            return mxv - mnv

        pq = []

        for l in range(n):
            v = value(l, n - 1)
            heapq.heappush(pq, (-v, l, n - 1))

        ans = 0

        for _ in range(k):
            neg_v, l, r = heapq.heappop(pq)
            ans += -neg_v

            if r > l:
                nv = value(l, r - 1)
                heapq.heappush(pq, (-nv, l, r - 1))

        return ans