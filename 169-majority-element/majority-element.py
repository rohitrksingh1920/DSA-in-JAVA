class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)
        count = 0
        res = 0

        for curr in nums:
            if count == 0:
                res = curr
            if res == curr:
                count += 1

            else:
                count -= 1

        return res














        # n = len(nums)
        # count = 0
        # res = 0
        # for curr in nums:
        #     if count == 0:
        #         res = curr
        #     if curr == res:
        #         count += 1
        #     else:
        #         count -= 1

        # return res