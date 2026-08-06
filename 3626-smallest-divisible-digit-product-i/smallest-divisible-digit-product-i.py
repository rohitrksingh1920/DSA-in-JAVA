class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digitProduct(x):
            prod = 1
            while x > 0:
                prod *= x % 10
                x //= 10
            return prod

        while True:
            if digitProduct(n) % t == 0:
                return n
            n += 1