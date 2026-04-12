class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        
        n = len(nums)
        minDis = float('inf')

        for i in range(n):
            count = 1
            prev = i

            for j in range(i + 1, n):
                if nums[j] == nums[i]:
                    count += 1

                    if count == 2:
                        mid = j
                    elif count == 3:
                        k = j
                        dis = (mid - i) + (k - mid) + (k - i)
                        minDis = min(minDis, dis)
                        break

        return minDis if minDis != float('inf') else -1