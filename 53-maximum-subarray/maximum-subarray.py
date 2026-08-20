class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):
            curSum = max(nums[i], curSum + nums[i])
            maxSum = max(maxSum, curSum)

        return maxSum



        # maxSum = nums[0]
        # n = len(nums)

        # for i in range(n):
        #     curSum = 0
        #     for j in range(i, n):
        #         curSum += nums[j]
        #         maxSum = max(maxSum, curSum)

        # return maxSum