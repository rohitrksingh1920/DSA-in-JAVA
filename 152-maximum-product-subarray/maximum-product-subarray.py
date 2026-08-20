class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxPro = nums[0]
        for i in range(len(nums)):
            curPro = 1
            for j in range(i, len(nums)):
                curPro *= nums[j]
                if curPro > maxPro:
                    maxPro = curPro

        return maxPro