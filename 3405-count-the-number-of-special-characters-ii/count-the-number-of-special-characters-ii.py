class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lastLower = {}
        firstUpper = {}

        for i, ch in enumerate(word):
            if ch.islower():
                lastLower[ch] = i
            else:
                lowerCh = ch.lower()
                if lowerCh not in firstUpper:
                    firstUpper[lowerCh] = i

        count = 0

        for ch in lastLower:
            if ch in firstUpper and lastLower[ch] < firstUpper[ch]:
                count += 1

        return count