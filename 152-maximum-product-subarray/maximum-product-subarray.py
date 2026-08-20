class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        maxPro = nums[0]

        n = len(nums)

        for i in range(1, n):
            prevMax = curMax
            prevMin = curMin

            curMax = max(nums[i], nums[i] * prevMin, nums[i] * prevMax)
            curMin = min(nums[i], nums[i] * prevMin, nums[i] * prevMax)

            maxPro = max(maxPro, curMax)

        return maxPro