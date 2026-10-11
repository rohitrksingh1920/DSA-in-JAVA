class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        res = 0

        for i in range(n):
            if count == 0:
                res = nums[i]

            if res == nums[i]:
                count += 1

            else:
                count -= 1

        return res
