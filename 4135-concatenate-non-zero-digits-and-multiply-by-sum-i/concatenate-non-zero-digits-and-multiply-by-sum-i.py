class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num1 = 0
        while n > 0:
            digit = n % 10
            if digit != 0:
                num1 = num1 * 10 + digit
            n = n // 10
        
        x = 0
        sum = 0
        while num1 > 0:
            digit = num1 % 10
            sum += digit
            x = x * 10 + digit

            num1 = num1 // 10

        return x * sum

         
                