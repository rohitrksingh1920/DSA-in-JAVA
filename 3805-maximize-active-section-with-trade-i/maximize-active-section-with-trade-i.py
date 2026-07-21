class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)

        totalOnes = s.count("1")

        t = "1" + s + "1"
        m = len(t)

        groups = []
        i = 0

        while i < m:
            j = i
            while j < m and t[j] == t[i]:
                j += 1

            groups.append((t[i], j - i))
            i = j

        gain = 0

        for i in range(1, len(groups) - 1):
            if (groups[i][0] == "1" and
                groups[i - 1][0] == "0" and
                groups[i + 1][0] == "0"):
                gain = max(
                    gain,
                    groups[i - 1][1] + groups[i + 1][1]
                )

        return totalOnes + gain