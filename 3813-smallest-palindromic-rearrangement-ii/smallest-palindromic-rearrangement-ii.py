class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        half = [0] * 26
        mid = ""

        m = 0
        for c, f in cnt.items():
            half[ord(c) - 97] = f // 2
            m += f // 2
            if f & 1:
                mid = c

        ways = 1
        rem = m
        for f in half:
            if f:
                ways *= comb(rem, f)
                rem -= f

        if ways < k:
            return ""

        ans = []

        while m:
            for c in range(26):
                if half[c] == 0:
                    continue

                nxt = ways * half[c] // m

                if nxt >= k:
                    ans.append(chr(c + 97))
                    ways = nxt
                    half[c] -= 1
                    m -= 1
                    break

                k -= nxt

        left = "".join(ans)
        return left + mid + left[::-1]