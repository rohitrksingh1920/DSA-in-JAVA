class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:

        n = len(points)

        points2 = []

        for x, y in points:
            if y == 0:
                points2.append(x)
            elif y == side:
                points2.append(side * 2 + (side - x))
            elif x == 0:
                points2.append(side * 3 + (side - y))
            elif x == side:
                points2.append(side + y)
            
        points2.sort()

        def check(mn):
            for i in range(n):
                count = 1
                curr = i
                while count < k:
                    jump = bisect.bisect_left(points2, points2[curr] + mn)

                    if jump == len(points2):
                        return False

                    if points2[i] + 4 * side - points2[jump] < mn:
                        break

                    count += 1
                    curr = jump

                if count == k:
                    return True
            return False
        
        l = 1
        h = side * 2
        while l < h:
            mid = l + (h - l + 1) // 2

            if check(mid):
                l = mid
            else:
                h = mid - 1

        return l







        # def mapPoint(x, y):
        #     if y == 0:
        #         return x
        #     elif x == side:
        #         return side + y
        #     elif y == side:
        #         return 3 * side - x
        #     else:
        #         return 4 * side - y
        
        # arr = sorted(mapPoint(x, y) for x, y in points)
        # n = len(arr)
        # perimeter = 4 * side

        # arr2 = arr + [x + perimeter for x in arr]

        # def can(d):
        #     for i in range(n):
        #         count = 1
        #         last = arr2[i]

        #         for j in range(i + 1, i + n):
        #             if arr2[j] - last >= d:
        #                 count += 1
        #                 last = arr2[j]
        #                 if count >= k:
        #                     if arr2[i] + perimeter - last >= d:
        #                         return True
        #                     else:
        #                         break
        #     return False

        # left, right = 0, perimeter
        # ans = 0

        # while left <= right:
        #     mid = (left + right) // 2

        #     if can(mid):
        #         ans = mid
        #         left = mid + 1
        #     else:
        #         right = mid - 1

        # return ans