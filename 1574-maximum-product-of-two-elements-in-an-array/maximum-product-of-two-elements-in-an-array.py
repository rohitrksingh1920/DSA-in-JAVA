class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxPro = 0
        nums.sort()
        maxPro = max(maxPro, ((nums[n-1])-1) * ((nums[n-2])-1), ((nums[0])-1) * ((nums[1])-1))

        return maxPro