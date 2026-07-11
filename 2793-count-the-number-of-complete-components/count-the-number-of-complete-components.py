class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        vis = [False] * n
        ans = 0

        for i in range(n):
            if vis[i]:
                continue

            q = deque([i])
            vis[i] = True
            nodes = []

            while q:
                node = q.popleft()
                nodes.append(node)

                for nei in graph[node]:
                    if not vis[nei]:
                        vis[nei] = True
                        q.append(nei)

            k = len(nodes)
            edgeCount = 0

            for node in nodes:
                edgeCount += len(graph[node])

            edgeCount //= 2

            if edgeCount == k * (k - 1) // 2:
                ans += 1

        return ans