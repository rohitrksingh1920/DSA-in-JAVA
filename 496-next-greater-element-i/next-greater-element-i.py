class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []

        for val in nums1:
            idx = nums2.index(val)
            nextGreater = -1

            for i in range(idx + 1, len(nums2)):
                if nums2[i] > val:
                    nextGreater = nums2[i]
                    break

            ans.append(nextGreater)

        return ans