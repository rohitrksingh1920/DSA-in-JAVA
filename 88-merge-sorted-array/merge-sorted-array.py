class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0
        k = 0

        arr = [0] * (m + n)

        # merge both arrays into arr
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                arr[k] = nums1[i]
                i += 1
            else:
                arr[k] = nums2[j]
                j += 1
            k += 1

        # copy remaining elements of nums2
        while j < n:
            arr[k] = nums2[j]
            j += 1
            k += 1

        # copy remaining elements of nums1
        while i < m:
            arr[k] = nums1[i]
            i += 1
            k += 1

        # copy merged result back to nums1
        for x in range(m + n):
            nums1[x] = arr[x]

        # i = 0
        # j = 0
        # k = 0

        # arr = [0] * (n+m)

        # while i < m and j < n:
        #     if nums1[i] < nums2[j]:
        #         arr[k] nums1[i]
        #         i += 1
        #     else:
        #         arr[k] = nums2[j]
        #         j +=1

        #     k +=1

        # while j < n:
        #     arr[k] = nums2[j]
        #     j += 1
        #     k += 1

        # while i < m:
        #     arr[k] = nums[i]
        #     i += 1
        #     k += 1

        # arr[] = nums[i]