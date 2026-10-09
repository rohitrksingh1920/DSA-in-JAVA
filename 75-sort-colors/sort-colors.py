class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # zero = 0
        # one = 0
        # two = 0

        # for val in nums:
        #     if val == 0:
        #         zero += 1
        #     elif val == 1:
        #         one += 1
        #     else:
        #         two += 1

        # for i in range(0, zero):
        #     nums[i] = 0

        # for i in range(zero, zero + one):
        #     nums[i] = 1

        # for i in range(zero + one, zero + one + two):
        #     nums[i] = 2


        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1