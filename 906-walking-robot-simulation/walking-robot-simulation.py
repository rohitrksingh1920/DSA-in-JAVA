class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        
        x, y = 0, 0
        obstacleSet = set(map(tuple, obstacles))
        
        maxDistance = 0
        
        for cmd in commands:
            if cmd == -1:  
                d = (d + 1) % 4
            elif cmd == -2:  
                d = (d - 1) % 4
            else:
                dx, dy = directions[d]
                for _ in range(cmd):
                    if (x + dx, y + dy) in obstacleSet:
                        break
                    x += dx
                    y += dy
                    maxDistance = max(maxDistance, x*x + y*y)
        
        return maxDistance