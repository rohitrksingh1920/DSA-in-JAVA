class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 3 different binary search 1 minValue in rotated array, then one on left and one on right of that minValue of 1st binary serach

        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1

                else:
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                else:
                    right = mid - 1

        return -1