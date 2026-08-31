class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # for i in range(0, n):
        #     for j in range(1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        freq = {}
        for i in range(n):
            needed = target - nums[i]
            if needed in freq:
                return [freq[needed], i]

            freq[nums[i]] = i