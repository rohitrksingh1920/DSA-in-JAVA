class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        n = len(nums)

        total = sum(nums)
        left = 0

        for i in range(n):
            right = total - left - nums[i]

            if right == left:
                return i

            else:
                left += nums[i]

        return -1