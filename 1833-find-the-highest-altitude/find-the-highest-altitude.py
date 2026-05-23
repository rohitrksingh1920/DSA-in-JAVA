class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)

        ps = [0] * (n + 1)

        for i in range(n):
            ps[i] = ps[i-1] + gain[i]

        return max(ps)