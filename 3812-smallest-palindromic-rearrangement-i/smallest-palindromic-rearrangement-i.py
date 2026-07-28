class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = Counter(s)
        left = []
        mid = ""

        for ch in sorted(cnt):
            left.append(ch * (cnt[ch] // 2))
            if cnt[ch] % 2:
                mid = ch

        left = "".join(left)
        return left + mid + left[::-1]