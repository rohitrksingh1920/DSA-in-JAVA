class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree = [0] * (4 * n)
        sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, l, r, val):
            length = r - l + 1
            sq[node] = (sq[node] + 2 * val * tree[node]
                        + length * val * val) % MOD
            tree[node] = (tree[node] + length * val) % MOD
            lazy[node] += val

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return

            mid = (l + r) // 2
            val = lazy[node]

            apply(node * 2, l, mid, val)
            apply(node * 2 + 1, mid + 1, r, val)
            lazy[node] = 0

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(node, l, r, 1)
                return

            push(node, l, r)
            mid = (l + r) // 2

            if ql <= mid:
                update(node * 2, l, mid, ql, qr)

            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr)

            tree[node] = (tree[node * 2] +
                          tree[node * 2 + 1]) % MOD
            sq[node] = (sq[node * 2] +
                        sq[node * 2 + 1]) % MOD

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return sq[node]

            push(node, l, r)
            mid = (l + r) // 2
            result = 0

            if ql <= mid:
                result += query(node * 2, l, mid, ql, qr)

            if qr > mid:
                result += query(node * 2 + 1, mid + 1, r,
                                ql, qr)

            return result % MOD

        last = {}
        ans = 0

        for i, num in enumerate(nums):
            prev = last.get(num, -1)

            update(1, 0, n - 1, prev + 1, i)
            ans = (ans + query(1, 0, n - 1, 0, i)) % MOD

            last[num] = i

        return ans
