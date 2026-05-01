class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        
        totalSum = sum(nums)
        F = sum(i * num for i, num in enumerate(nums))
        
        maxVal = F
        
        for k in range(1, n):
            F = F + totalSum - n * nums[n - k]
            maxVal = max(maxVal, F)
        
        return maxVal