class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        # for i in nums:
        #     count = 0

        #     for j in range(n):
        #         if nums[j] == i:
        #             count += 1

        #     if count > n // 2:
        #         return i
        

        freq = {}

        for curr in nums:
            if curr in freq:
                freq[curr] += 1
            else:
                freq[curr] = 1

            if freq[curr] > n // 2:
                return curr