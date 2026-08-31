class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        def reverseArray(s, e):
            while s < e:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e -= 1

        reverseArray(0, n - 1)
        reverseArray(0, k - 1)
        reverseArray(k, n - 1)
        