class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxEle = max(nums)
        moves = 0

        for num in nums:
            moves += maxEle - num

        return moves