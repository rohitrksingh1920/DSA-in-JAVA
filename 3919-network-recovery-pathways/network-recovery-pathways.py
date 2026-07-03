class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        lo = inf
        hi = 0

        for u, v, w in edges:
            if not online[u] or not online[v]:
                continue

            graph[u].append((v, w))
            lo = min(lo, w)
            hi = max(hi, w)

        if lo == inf:
            return -1

        def check(limit):
            dist = [inf] * n
            dist[0] = 0

            pq = [(0, 0)]

            while pq:
                cost, node = heappop(pq)

                if cost > dist[node]:
                    continue

                if cost > k:
                    continue

                if node == n - 1:
                    return True

                for nxt, w in graph[node]:
                    if w < limit:
                        continue

                    newCost = cost + w

                    if newCost < dist[nxt]:
                        dist[nxt] = newCost
                        heappush(pq, (newCost, nxt))

            return False

        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2

            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans