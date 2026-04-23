class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        arr = [0]*n

        # for i in range(n):
        #     sum = 0
        #     for j in range(n):
        #         if nums[i] == nums[j] and i != j:
        #             sum += abs(i-j)
        #     arr[i] = sum
            
        # return arr

        
        count = defaultdict(int)
        total = defaultdict(int)
        
        for i in range(n):
            x = nums[i]
            arr[i] += count[x] * i - total[x]
            count[x] += 1
            total[x] += i
        
        count.clear()
        total.clear()
        
        for i in range(n - 1, -1, -1):
            x = nums[i]
            arr[i] += total[x] - count[x] * i
            count[x] += 1
            total[x] += i
        
        return arr