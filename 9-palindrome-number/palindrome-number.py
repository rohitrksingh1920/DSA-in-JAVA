class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        original = x
        sign = 1
        if x < 0:
            return False

        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10

        if rev == original:
            return True
        else:
            return False