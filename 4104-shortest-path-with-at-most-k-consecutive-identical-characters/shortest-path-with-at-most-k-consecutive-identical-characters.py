class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))

        # dist[node][count] = minimum distance
        dist = [[float('inf')] * (k + 1) for _ in range(n)]

        pq = [(0, 0, 1)]
        dist[0][1] = 0

        while pq:
            cost, node, count = heapq.heappop(pq)

            if cost != dist[node][count]:
                continue

            if node == n - 1:
                return cost

            for nei, weight in adj[node]:

                if labels[node] == labels[nei]:
                    newCount = count + 1
                else:
                    newCount = 1

                if newCount > k:
                    continue

                newCost = cost + weight

                if newCost < dist[nei][newCount]:
                    dist[nei][newCount] = newCost
                    heapq.heappush(
                        pq, (newCost, nei, newCount)
                    )

        return -1
