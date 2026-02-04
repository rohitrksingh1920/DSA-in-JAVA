class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverseArray(nums, s, e):
            while s < e:
                nums[s], nums[e] = nums[e] , nums[s]
                s += 1
                e -= 1

        # 1. revers

        k = k % len(nums)
        reverseArray(nums, 0, len(nums)-1)
        print(nums)

        reverseArray(nums, 0, k-1)
        print(nums)

        reverseArray(nums, k, len(nums)-1)
        print(nums)

        