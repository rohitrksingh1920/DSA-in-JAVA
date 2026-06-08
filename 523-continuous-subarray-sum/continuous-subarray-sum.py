class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dict = {0: -1}
        prefixSum = 0

        for i in range(len(nums)):
            prefixSum += nums[i]
            rem = prefixSum % k

            if rem in dict:
                if i - dict[rem] >= 2:
                    return True
            else:
                dict[rem] = i

        return False