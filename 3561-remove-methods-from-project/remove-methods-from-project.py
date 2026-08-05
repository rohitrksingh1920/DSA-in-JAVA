class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)

        suspicious = [False] * n

        def dfs(u):
            suspicious[u] = True
            for v in graph[u]:
                if not suspicious[v]:
                    dfs(v)

        # Mark all suspicious methods
        dfs(k)

        # If any non-suspicious method calls a suspicious one,
        # we cannot remove the suspicious methods.
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        # Otherwise, keep only the non-suspicious methods.
        ans = []
        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans