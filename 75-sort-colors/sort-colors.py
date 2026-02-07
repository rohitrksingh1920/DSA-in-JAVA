class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        one = 0
        two = 0

        for val in nums:
            if val == 0:
                zero += 1
            elif val == 1:
                one += 1
            else:
                two += 1

        for i in range(0, zero):
            nums[i] = 0

        for i in range(zero, zero + one):
            nums[i] = 1

        for i in range(zero + one, zero + one + two):
            nums[i] = 2


        # zero = 0
        # curr = 0
        # two = len(nums) - 1

        # while curr <= two:
        #     if nums[curr] == 0:
        #         nums[zero], nums[curr] = nums[curr], nums[zero]
        #         zero += 1
        #         curr += 1

        #     elif nums[curr] == 2:
        #         nums[curr], nums[two] = nums[two], nums[curr]
        #         two -= 1

        #     else:
        #         curr += 1
