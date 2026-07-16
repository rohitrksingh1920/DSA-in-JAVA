class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []

        mx = 0
        for x in nums:
            mx = max(mx, x)
            prefixGcd.append(gcd(x, mx))

        prefixGcd.sort()

        i = 0
        j = len(prefixGcd) - 1

        ans = 0

        while i < j:
            ans += gcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1

        return ans