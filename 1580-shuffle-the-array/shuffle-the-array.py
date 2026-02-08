class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        start = 0
        mid = n

        arr = [0] * (len(nums))

        for i in range(0, len( nums)):
            if i % 2 == 0:
                arr[i] = nums[start]
                start += 1
            else:
                arr[i] = nums[mid]
                mid += 1

        return arr