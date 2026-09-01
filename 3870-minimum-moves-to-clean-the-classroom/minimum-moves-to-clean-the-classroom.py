from collections import deque
from typing import List
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        
        m = len(classroom)
        n = len(classroom[0])

        # Store starting position and give every L a unique index
        litter = {}
        start_r = start_c = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start_r, start_c = i, j

                elif classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)

        # No litter to collect
        if len(litter) == 0:
            return 0

        # All litter collected mask
        full_mask = (1 << len(litter)) - 1

        # (row, col, collected_mask, remaining_energy)
        queue = deque()
        queue.append((start_r, start_c, 0, energy))

        visited = set()
        visited.add((start_r, start_c, 0, energy))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        moves = 0

        while queue:
            size = len(queue)

            for _ in range(size):
                r, c, mask, curr_energy = queue.popleft()

                # All litter collected
                if mask == full_mask:
                    return moves

                # Cannot move without energy
                if curr_energy == 0:
                    continue

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Check boundaries and obstacles
                    if (
                        nr < 0 or nr >= m or
                        nc < 0 or nc >= n or
                        classroom[nr][nc] == 'X'
                    ):
                        continue

                    # Moving costs 1 energy
                    new_energy = curr_energy - 1
                    new_mask = mask

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    # Collect litter
                    elif classroom[nr][nc] == 'L':
                        bit = litter[(nr, nc)]
                        new_mask |= (1 << bit)

                    state = (nr, nc, new_mask, new_energy)

                    if state not in visited:
                        visited.add(state)
                        queue.append(state)

            moves += 1

        return -1