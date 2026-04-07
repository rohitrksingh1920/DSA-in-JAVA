class Solution:
    def nextSmallerElement(self, heights):
        n = len(heights)
        res = [n]*n

        stack = []

        for i in range(n-1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(i)
        return res

    def prevSmallerElement(self, heights):
        n = len(heights)
        res = [-1]*n

        stack = []

        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(i)
        return res
        
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        nse = self.nextSmallerElement(heights)
        pse = self.prevSmallerElement(heights)

        ans = 0

        for i in range(n):
            width = nse[i] - pse[i] - 1

            currArea = heights[i] * width
            ans = max(ans, currArea)
        return ans

