class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        freq = {}

        for i in range(n):
            needed = target - nums[i]

            if needed in freq:
                return [freq[needed], i]

            freq[nums[i]] = i