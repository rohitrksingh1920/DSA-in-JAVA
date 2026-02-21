class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        # count = 0
        
        # while left <= right:
        #     num = left
        #     bits = 0
            
        #     while num > 0:
        #         if num % 2 == 1:
        #             bits += 1
        #         num = num // 2
            
        #     if bits > 1:
        #         is_prime = True
        #         for i in range(2, bits):
        #             if bits % i == 0:
        #                 is_prime = False
        #                 break
        #         if is_prime:
        #             count += 1
            
        #     left += 1
        
        # return count

        count = 0
        while left <= right:
            temp = left
            bits = 0

            while temp > 0:
                if temp % 2 == 1:
                    bits += 1
                
                temp = temp // 2
        
            if bits > 1:
                isPrime = True
                for i in range(2, bits):
                    if bits % i == 0:
                        isPrime = False
                        break
                if isPrime:
                    count += 1
            left += 1
        return count