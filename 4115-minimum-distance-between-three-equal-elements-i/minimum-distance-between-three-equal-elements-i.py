class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        
        n = len(nums)
        minDis = float('inf')

        for j in range(n):
            i = -1
            k = -1

            for left in range(j - 1, -1, -1):
                if nums[left] == nums[j]:
                    i = left
                    break

            for right in range(j + 1, n):
                if nums[right] == nums[j]:
                    k = right
                    break

            if i != -1 and k != -1:
                dis = (j - i) + (k - j) + (k - i)
                minDis = min(minDis, dis)

        return minDis if minDis != float('inf') else -1