class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n = len(nums)
        # freq = {}
        # for i in range(n):
        #     needed = target - nums[i]
        #     if needed in freq:
        #         return [freq[needed], i]

        #     freq[nums[i]] = i



        # arr = sort(nums)
        # n = len(arr)

        # left = 0
        # right = n - 1

        # while left < right:
        #     mid = (left + right) // 2
        #     if arr[left] + arr[right] == target:
        #         return [left, right]
        #     if arr[left] + arr [right] > target:
        #         right -= 1 

        #     else:
        #         left += 1

        arr = sorted((num, i) for i, num in enumerate(nums))

        left = 0
        right = len(arr) - 1

        while left < right:
            total = arr[left][0] + arr[right][0]

            if total == target:
                return [arr[left][1], arr[right][1]]

            elif total > target:
                right -= 1

            else:
                left += 1
