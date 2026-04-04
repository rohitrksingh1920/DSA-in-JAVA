class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        if n == 0:
            return 0

        leftGre = [0] * n
        rightGre = [0] * n

        leftGre[0] = height[0]
        for i in range(1, n):
            leftGre[i] = max(leftGre[i-1], height[i])

        rightGre[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            rightGre[i] = max(rightGre[i+1], height[i])

        water = 0
        for i in range(n):
            water += min(leftGre[i], rightGre[i]) - height[i]

        return water