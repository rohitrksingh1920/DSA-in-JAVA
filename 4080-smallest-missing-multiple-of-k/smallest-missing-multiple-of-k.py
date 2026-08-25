class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = len(nums)
        numSet = set(nums)
        mul = k
        for i in range(1, n + 2):
            mul = k * i

            if mul not in numSet:
                return mul



        