class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # i = 0

        # for j in range(1, len(nums)):
        #     lastUnique = nums[i]
        #     curr = nums[j]

        #     if nums[i] != nums[j]:
        #         nums[i+1] = nums[j]
        #         i += 1

        # return i + 1



        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k
