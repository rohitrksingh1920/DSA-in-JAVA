class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        new_list = []
        arr.sort()

        minAbsDiff = float('inf')

        for i in range(1, len(arr)):
            minAbsDiff = min(minAbsDiff, arr[i] - arr[i-1])

        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == minAbsDiff:
                new_list.append([arr[i-1], arr[i]])

        return new_list
