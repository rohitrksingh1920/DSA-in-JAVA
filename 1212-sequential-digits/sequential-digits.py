class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = "123456789"
        ans = []

        lowLen = len(str(low))
        highLen = len(str(high))

        for length in range(lowLen, highLen + 1):
            for i in range(10 - length):
                num = int(nums[i:i + length])

                if low <= num <= high:
                    ans.append(num)

        return ans