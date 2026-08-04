class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        present = set(nums)
        ans = []

        for i in range(min(nums), max(nums) + 1):
            if i not in nums:
                ans.append(i)

        return ans