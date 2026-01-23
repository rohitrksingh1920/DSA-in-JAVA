class Solution:
    def reverse(self, x: int) -> int:

        rev = 0
        sign = 1
        original = x
        maxLimit = 2**31 - 1
        minLimit = -2**31

        if x < 0:
            sign = -1
            x = abs(x)

        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10

        if rev > maxLimit or rev < minLimit:
            return 0
        else:
            return rev * sign
        