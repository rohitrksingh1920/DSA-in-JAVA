class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)

        ans = 1

        if 1 in freq:
            if freq[1] % 2 == 0:
                ans = freq[1] - 1
            else:
                ans = freq[1]

        for x in list(freq.keys()):
            if x == 1:
                continue

            cur = x
            length = 0

            while freq[cur] >= 2:
                length += 2
                cur = cur * cur

                if cur not in freq:
                    break

            if freq.get(cur, 0) >= 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans