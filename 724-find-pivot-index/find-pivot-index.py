class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        ps = [0] * n
        ps[0] = nums[0]

        for i in range(1, n):
            ps[i] = ps[i - 1] + nums[i]

        totalSum = ps[n - 1]

        for i in range(n):

            if i == 0:
                leftSum = 0
            else:
                leftSum = ps[i - 1]

            rightSum = totalSum - ps[i]

            if leftSum == rightSum:
                return i

        return -1