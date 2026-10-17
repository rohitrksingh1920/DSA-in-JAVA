class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digitSum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

        n = len(nums)

        arr = sorted((digitSum(num), num, i)
                     for i, num in enumerate(nums))

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or arr[i][2] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps
