class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = [False] * (n + 1)
        q = deque([1])
        visited[1] = True
        ans = float("inf")

        while q:
            node = q.popleft()

            for nei, w in graph[node]:
                ans = min(ans, w)
                if not visited[nei]:
                    visited[nei] = True
                    q.append(nei)

        return ans