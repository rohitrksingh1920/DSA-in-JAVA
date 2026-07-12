class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedUniqArr = sorted(set(arr))
        n = len(sortedUniqArr)
        rank = {}
        ans = []

        for i in range(n):
            rank[sortedUniqArr[i]] = i + 1

        for val in arr:
            ans.append(rank[val])

        return ans