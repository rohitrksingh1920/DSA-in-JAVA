class Solution:
    def trap(self, height: List[int]) -> int:
        # n = len(height)
        # if n == 0:
        #     return 0
        # leftGre = [0] * n
        # rightGre = [0] * n

        # leftGre[0] = height[0]
        # for i in range(1, n):
        #     leftGre[i] = max(leftGre[i-1], height[i])

        # rightGre[n-1] = height[n-1]
        # for i in range(n-2, -1, -1):
        #     rightGre[i] = max(rightGre[i+1], height[i])

        # water = 0
        # for i in range(n):
        #     water += min(leftGre[i], rightGre[i]) - height[i]

        # return water











        left = 0
        right = len(height) - 1

        leftMax = 0
        rightMax = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    water += leftMax - height[left]
                left += 1

            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    water += rightMax - height[right]
                right -= 1

        return water