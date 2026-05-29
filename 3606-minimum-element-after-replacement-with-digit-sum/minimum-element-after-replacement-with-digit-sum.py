class Solution:
    def minElement(self, nums: List[int]) -> int:
        sumArr = []
        for val in nums:
            digitSum = 0
            while val > 0:
                digitSum += val % 10
                val //= 10

            sumArr.append(digitSum)

        return min(sumArr)