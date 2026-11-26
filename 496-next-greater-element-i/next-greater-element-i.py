class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        next_greater = {}

        for num in nums2:

            while stack and stack[-1] < num:
                smaller = stack.pop()
                next_greater[smaller] = num

            stack.append(num)

        result = []

        for num in nums1:
            if num in next_greater:
                result.append(next_greater[num])
            else:
                result.append(-1)

        return result
