class Solution:
    def concatenatedBinary(self, n: int) -> int:
        modulo = 10**9 + 7
        result = 0
    
        for i in range(1, n + 1):
        
            bits = 0
            num = i
            while num > 0:
                bits += 1
                num //= 2
        
            result = (result << bits) | i
        
            result %= modulo
    
        return result