class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        
        queue = deque([start])
        visited[start] = True
        
        while queue:
            idx = queue.popleft()
            
            if arr[idx] == 0:
                return True
            
            forward = idx + arr[idx]
            if forward < n and not visited[forward]:
                visited[forward] = True
                queue.append(forward)
            
            backward = idx - arr[idx]
            if backward >= 0 and not visited[backward]:
                visited[backward] = True
                queue.append(backward)
        
        return False