class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0

        for j in range(1, len(nums)):
            lastUnique = nums[i]
            curr = nums[j]

            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1

        return i + 1