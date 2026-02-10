class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLen = 0
        count = 0

        for val in nums:
            if val == 1:
                count += 1
                maxLen = max(maxLen, count)
            else:
                count = 0

        return maxLen
            