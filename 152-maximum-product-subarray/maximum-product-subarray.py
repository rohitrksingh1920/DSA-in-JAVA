class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        currMax = nums[0]
        currMin = nums[0]
        maxPro = nums[0]

        for i in range(1, n):
            temp = max(nums[i], nums[i]*currMax, nums[i]*currMin)
            currMin = min(nums[i], nums[i]*currMax, nums[i]*currMin)

            currMax = temp

            maxPro = max(maxPro, currMax)

        return maxPro




















        # currMax = nums[0]
        # currMin = nums[0]
        # maxPro = nums[0]

        # n = len(nums)

        # for i in range(1, n):
        #     tempMax = max(nums[i], nums[i]*currMax, nums[i]*currMin)
        #     currMin = min(nums[i], nums[i]*currMax, nums[i]*currMin)

        #     currMax = tempMax

        #     maxPro = max(maxPro, currMax)

        # return maxPro
