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

        right = 0
        maxLen = 0

        for val in nums:
            if val == 1:
                right += 1
                maxLen = max(maxLen, right)
            else:
                right = 0

        return maxLen