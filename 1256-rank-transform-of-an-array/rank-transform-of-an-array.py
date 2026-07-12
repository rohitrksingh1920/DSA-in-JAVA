class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedArr = sorted(set(arr))

        rank = {}
        for i in range(len(sortedArr)):
            rank[sortedArr[i]] = i + 1

        ans = []
        for val in arr:
            ans.append(rank[val])

        return ans