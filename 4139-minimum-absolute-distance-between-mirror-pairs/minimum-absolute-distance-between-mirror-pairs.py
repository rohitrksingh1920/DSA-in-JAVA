class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        
        def reverse(x):
            return int(str(x)[::-1])
        seen = {}
        n = len(nums)
        minDis = float('inf')
        
        for i in range(n):
            num = nums[i]
            if num in seen:
                minDis = min(minDis, i-seen[num])
            rev = reverse(num)
            seen[rev] = i
        
        return minDis if minDis != float('inf') else -1
            