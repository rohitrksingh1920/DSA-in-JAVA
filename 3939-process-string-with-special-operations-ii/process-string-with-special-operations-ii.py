class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)

        lengths = [0] * (n + 1)

        for i, ch in enumerate(s):
            cur = lengths[i]

            if ch.islower():
                lengths[i + 1] = min(10**18, cur + 1)
            elif ch == '*':
                lengths[i + 1] = max(0, cur - 1)
            elif ch == '#':
                lengths[i + 1] = min(10**18, cur * 2)
            else:  
                lengths[i + 1] = cur

        if k >= lengths[n]:
            return "."

        for i in range(n - 1, -1, -1):
            ch = s[i]
            prev = lengths[i]

            if ch.islower():
                if k == prev:
                    return ch

            elif ch == '*':
                if lengths[i + 1] < prev and k == prev - 1:
                    return "."

            elif ch == '#':
                if k >= prev:
                    k -= prev

            else:  
                k = prev - 1 - k

        return "."