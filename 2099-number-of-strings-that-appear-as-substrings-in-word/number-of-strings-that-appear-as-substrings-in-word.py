class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        n = len(patterns)
        count = 0
        for i in range(n):
            if patterns[i] in word:
                count += 1
        return count
