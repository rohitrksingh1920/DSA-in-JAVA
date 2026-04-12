class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        
        n = len(nums)
        minDis = float('inf')

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] != nums[j]:
                    continue
                for k in range(j + 1, n):
                    if nums[j] == nums[k]:
                        dis = (j - i) + (k - j) + (k - i)
                        minDis = min(minDis, dis)

        return minDis if minDis != float('inf') else -1