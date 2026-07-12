class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedUniArr = sorted(set(arr))

        rank = {}
        for i in range(len(sortedUniArr)):
            rank[sortedUniArr[i]] = i + 1

        ans = []
        for val in arr:
            ans.append(rank[val])

        return ans