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


        lo = 0
        mid = 0
        hi = len(nums) - 1

        while mid <= hi:
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1

            elif nums[mid] == 2:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1

            else:
                mid += 1
