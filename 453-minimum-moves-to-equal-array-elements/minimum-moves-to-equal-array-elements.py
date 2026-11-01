class Solution:
    def minMoves(self, nums: list[int]) -> int:
        n = len(nums)
        oper = 0
        minEle = min(nums)
        for i in range(n):
            oper += nums[i] - minEle

        return oper