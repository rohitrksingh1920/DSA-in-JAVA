class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minOdd = float('inf')

        for num in nums1:
            if num % 2 == 1:
                minOdd = min(minOdd, num)

        for num in nums1:
            if num % 2 == 0 and minOdd != float('inf') and num < minOdd:
                return False

        return True