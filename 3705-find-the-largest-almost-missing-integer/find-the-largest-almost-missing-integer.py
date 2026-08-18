class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = {}

        n = len(nums)

        for i in range(n - k + 1):
            seen = set()

            for j in range(i, i + k):
                if nums[j] not in seen:
                    count[nums[j]] = count.get(nums[j], 0) + 1
                    seen.add(nums[j])

        ans = -1

        for x in count:
            if count[x] == 1:
                ans = max(ans, x)

        return ans