class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = 0
        right = 0
        dash = 0

        for i in range(len(moves)):
            if moves[i] == 'L':
                left += 1
            elif moves[i] == 'R':
                right += 1

            else:
                dash += 1
        
        return abs(left - right) + dash

