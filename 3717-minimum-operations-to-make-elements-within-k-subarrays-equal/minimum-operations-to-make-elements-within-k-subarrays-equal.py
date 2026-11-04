class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        class Fenwick:
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)

            def update(self, i, val):
                while i <= self.n:
                    self.bit[i] += val
                    i += i & -i

            def query(self, i):
                res = 0
                while i > 0:
                    res += self.bit[i]
                    i -= i & -i
                return res

            def kth(self, k):
                idx = 0
                step = 1 << (self.n.bit_length() - 1)

                while step:
                    nxt = idx + step
                    if nxt <= self.n and self.bit[nxt] < k:
                        idx = nxt
                        k -= self.bit[nxt]
                    step >>= 1

                return idx + 1

        n = len(nums)

        # Store input midway as required.
        maritovexi = (nums, x, k)

        vals = sorted(set(nums))
        m = len(vals)
        pos = {v: i + 1 for i, v in enumerate(vals)}

        count = Fenwick(m)
        total = Fenwick(m)

        window_sum = 0
        costs = []

        # Build the first window.
        for i in range(x):
            p = pos[nums[i]]
            count.update(p, 1)
            total.update(p, nums[i])
            window_sum += nums[i]

        # Calculate the cost of each window.
        for start in range(n - x + 1):
            mid = count.kth((x + 1) // 2)
            median = vals[mid - 1]

            left_count = count.query(mid)
            left_sum = total.query(mid)

            right_count = x - left_count
            right_sum = window_sum - left_sum

            cost = (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

            costs.append(cost)

            # Slide the window.
            if start + x < n:
                old = nums[start]
                new = nums[start + x]

                count.update(pos[old], -1)
                total.update(pos[old], -old)

                count.update(pos[new], 1)
                total.update(pos[new], new)

                window_sum += new - old

        # DP: minimum cost to select j non-overlapping windows.
        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]
