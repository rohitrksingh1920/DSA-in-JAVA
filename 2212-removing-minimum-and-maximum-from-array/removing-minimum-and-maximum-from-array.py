class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        maximum = float('-inf')
        minimum = float('inf')

        idxMax = 0
        idxMin = 0

        for i in range(n):
            if nums[i] > maximum:
                maximum = nums[i]
                idxMax = i

            if nums[i] < minimum:
                minimum = nums[i]
                idxMin = i

        if idxMin > idxMax:
            idxMin, idxMax = idxMax, idxMin

        front = idxMax + 1
        back = n - idxMin
        both = (idxMin + 1) + (n - idxMax)

        return min(front, back, both)
            