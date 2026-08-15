class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        has_nonzero = False

        for x in nums:
            xor ^= x
            if x != 0:
                has_nonzero = True

        # If total XOR is already non-zero,
        # the whole array is the answer.
        if xor != 0:
            return len(nums)

        # If all elements are zero, no subsequence
        # can have non-zero XOR.
        if not has_nonzero:
            return 0

        # Total XOR is zero, but there is at least
        # one non-zero element. Remove one non-zero element.
        return len(nums) - 1