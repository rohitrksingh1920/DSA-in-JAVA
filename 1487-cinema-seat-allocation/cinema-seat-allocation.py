class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            
            rows[row].add(seat)

        ans = (n - len(rows)) * 2

        for seats in rows.values():

            left = True
            right = True
            middle = True

            for seat in range(2, 6):
                if seat in seats:
                    left = False

            for seat in range(6, 10):
                if seat in seats:
                    right = False

            for seat in range(4, 8):
                if seat in seats:
                    middle = False

            if left and right:
                ans += 2

            elif left or right or middle:
                ans += 1

        return ans