class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        nextGr8 = {}

        for num in nums2:

            while stack and stack[-1] < num:
                smaller = stack.pop()
                nextGr8[smaller] = num

            stack.append(num)

        result = []

        for num in nums1:
            if num in nextGr8:
                result.append(nextGr8[num])
            else:
                result.append(-1)

        return result
