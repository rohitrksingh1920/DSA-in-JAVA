class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        tree = [[1, [0] * k] for _ in range(4 * n)]

        def merge(left, right):
            leftProd, leftCnt = left
            rightProd, rightCnt = right

            prod = (leftProd * rightProd) % k
            cnt = leftCnt[:]

            for r in range(k):
                cnt[(leftProd * r) % k] += rightCnt[r]

            return [prod, cnt]

        def build(node, low, high):
            if low == high:
                value = nums[low] % k
                tree[node] = [value, [0] * k]
                tree[node][1][value] = 1
                return

            mid = (low + high) // 2

            build(node * 2, low, mid)
            build(node * 2 + 1, mid + 1, high)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, low, high, index, value):
            if low == high:
                value %= k
                tree[node] = [value, [0] * k]
                tree[node][1][value] = 1
                return

            mid = (low + high) // 2

            if index <= mid:
                update(node * 2, low, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, high, index, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, low, high, ql, qr):
            if ql <= low and high <= qr:
                return tree[node]

            mid = (low + high) // 2

            if qr <= mid:
                return query(node * 2, low, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, high, ql, qr)

            left = query(node * 2, low, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, high, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)

            result = query(1, 0, n - 1, start, n - 1)

            ans.append(result[1][x])

        return ans