class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter

        n = len(s)
        count = Counter(s)

        if sum(x % 2 for x in count.values()) > 1:
            return ""

        middle = ""
        for ch in count:
            if count[ch] % 2 == 1:
                middle = ch
                break

        half = [0] * 26

        for i in range(26):
            ch = chr(ord('a') + i)
            half[i] = count[ch] // 2

        left = []

        def possible():
            remaining = ""

            for i in range(25, -1, -1):
                remaining += chr(ord('a') + i) * half[i]

            left_part = ''.join(left) + remaining
            palindrome = left_part + middle + left_part[::-1]

            return palindrome > target

        for _ in range(n // 2):

            found = False

            for i in range(26):

                if half[i] == 0:
                    continue

                ch = chr(ord('a') + i)

                half[i] -= 1
                left.append(ch)

                if possible():
                    found = True
                    break

                left.pop()
                half[i] += 1

            if not found:
                return ""

        left_part = ''.join(left)
        answer = left_part + middle + left_part[::-1]

        return answer if answer > target else ""