class Solution:
    def maxProduct(self, n: int) -> int:
        newArr = []

        while n:
            digit = n % 10
            newArr.append(digit)
            n = n // 10

        maxPro = 0

        for i in range(len(newArr)):
            for j in range(i + 1, len(newArr)):
                maxPro = max(maxPro, newArr[i] * newArr[j])

        return maxPro