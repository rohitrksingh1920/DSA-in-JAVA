class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        # return goal in (s + s)

        
        for i in range(len(s)):
            rotated = s[i:] + s[:i]
            if rotated == goal:
                return True
        
        return False