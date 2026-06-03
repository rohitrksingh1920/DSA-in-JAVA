class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startVal = 1
        while True:
            stepSum = startVal
            valid = True

            for num in nums:
                stepSum += num

                if stepSum < 1:
                    valid = False
                    break

            if valid == True:
                return startVal

            startVal += 1