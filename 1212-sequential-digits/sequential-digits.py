class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        q = deque(range(1, 10))
        ans = []

        while q:
            num = q.popleft()

            if low <= num <= high:
                ans.append(num)

            last = num % 10

            if last < 9:
                nxt = num * 10 + last + 1
                if nxt <= high:
                    q.append(nxt)

        return ans