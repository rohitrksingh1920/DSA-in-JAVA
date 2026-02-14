class Solution:
    def sortArrayByParityII(self, nums):
        oddIndex = 1

        for evenIndex in range(0, len(nums), 2):

            if nums[evenIndex] % 2 != 0:

                while nums[oddIndex] % 2 != 0:
                    oddIndex += 2

                nums[evenIndex], nums[oddIndex] = nums[oddIndex], nums[evenIndex]

        return nums
