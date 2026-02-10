class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # maxLen = 0
        # count = 0

        # for val in nums:
        #     if val == 1:
        #         count += 1
        #         maxLen = max(maxLen, count)
        #     else:
        #         count = 0

        # return maxLen

        left = 0
        maxLen = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                left = right + 1
            
            maxLen = max(maxLen, right - left + 1)

        return maxLen