class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # total = sum(nums)
        # left = 0

        # for i in range(len(nums)):
        #     right = total - left - nums[i]

        #     if left == right:
        #         return i

        #     left += nums[i]

        # return -1

        total = sum(nums)
        left = 0
        n = len(nums)

        for i in range(n):
            right = total - left - nums[i]

            if right == left:
                return i

            left += nums[i]

        return -1