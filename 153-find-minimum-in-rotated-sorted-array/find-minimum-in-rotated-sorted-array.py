class Solution:
    def findMin(self, nums: List[int]) -> int:

        n = len(nums)

        nums.sort()
        return nums[0]