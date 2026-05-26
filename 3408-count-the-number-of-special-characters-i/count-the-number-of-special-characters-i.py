class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        lowerEle = set()
        upperEle = set()
        count = 0

        for char in word:
            if char.islower():
                lowerEle.add(char)
            elif char.isupper():
                upperEle.add(char.lower())
        for ch in lowerEle:
            if ch in upperEle:
                count += 1
        return count