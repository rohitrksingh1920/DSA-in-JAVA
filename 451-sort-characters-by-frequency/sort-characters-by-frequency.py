class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        arr = list(freq.keys())

        arr.sort(key=freq.get, reverse=True)

        
        result = ""

        for ch in arr:
            result += ch * freq[ch]

        return result
