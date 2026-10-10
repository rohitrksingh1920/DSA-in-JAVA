class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # freq = {}
        # for val in nums:
        #     if val in freq:
        #         freq[val] += 1
        #     else:
        #         freq[val] = 1

        # maxFreq = max(freq.values())
        # ans = 0

        # for val in freq.values():
        #     if val == maxFreq:
        #         ans += val

        # return ans













        freq = {}

        for val in nums:
            if val in freq:
                freq[val] += 1

            else:
                freq[val] = 1

        maxFreq = max(freq.values())
        ans = 0

        for val in freq.values():
            if val == maxFreq:
                ans += val
        return ans