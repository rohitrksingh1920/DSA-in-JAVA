class Solution:
    def mirrorDistance(self, n: int) -> int:
        
        original = n
        rev = 0
        while n > 0:
            digit = n % 10

            rev = rev*10 + digit

            n = n // 10
        mirrDis = abs(original - rev)
        return mirrDis