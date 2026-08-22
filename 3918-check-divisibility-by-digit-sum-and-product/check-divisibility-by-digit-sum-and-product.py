class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        digitSum = 0
        digitProduct = 1

        while temp > 0:
            digit = temp % 10
            digitSum += digit
            digitProduct *= digit
            temp //= 10

        return n % (digitSum + digitProduct) == 0