class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 3 different binary search 1 minvalue in rotated array, then one on left and one on right of that moin value of 1st binary serach


        # left = 0
        # right = len(nums) - 1

        # while left <= right:
        #     mid = (left + right) // 2

        #     if nums[mid] == target:
        #         return mid

        #     if nums[left] <= nums[mid]:

        #         if nums[left] <= target < nums[mid]:
        #             right = mid - 1
        #         else:
        #             left = mid + 1

        #     else:

        #         if nums[mid] < target <= nums[right]:
        #             left = mid + 1
        #         else:
        #             right = mid - 1

        # return -1






        # LineraSearch

        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i

        # return -1


        
        def pivotEle():
            lo = 0
            hi = len(nums) - 1
            while lo < hi:
                mid = (lo + hi) // 2

                if nums[mid] > nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid

            return lo

        def binarySearch(lo, hi):
            while lo <= hi:
                mid = (lo + hi) // 2

                if nums[mid] == target:
                    return mid

                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1

            return -1

        p = pivotEle()

        if nums[p] <= target <= nums[-1]:
            return binarySearch(p, len(nums) - 1)

        return binarySearch(0, p - 1)