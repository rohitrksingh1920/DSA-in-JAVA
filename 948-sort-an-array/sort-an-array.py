class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        if n <= 1:
            return nums

        mid = n // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        result = []

        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result


    #     n = len(nums)

    #     if n <= 1:
    #         return nums

    #     mid = n // 2

    #     left = self.sortArray(nums[:mid])
    #     right = self.sortArray(nums[mid:])

    #     return self.merge(left, right)

    # def merge(self, left, right):
    #     if not left:
    #         return right

    #     if not right:
    #         return left

    #     if left[0] <= right[0]:
    #         return [left[0]] + self.merge(left[1:], right)

    #     else:
    #         return [right[0]] + self.merge(left, right[1:])