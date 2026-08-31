class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        for val in nums:
            if val in freq:
                freq[val] += 1
            else:
                freq[val] = 1

        maxFreq = max(freq.values())
        ans = 0

        for cnt in freq.values():
            if cnt == maxFreq:
                ans += cnt

        return ans