class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        has_nonzero = False

        for x in nums:
            xor ^= x
            if x != 0:
                has_nonzero = True

        if xor != 0:
            return len(nums)

        if not has_nonzero:
            return 0

        return len(nums) - 1