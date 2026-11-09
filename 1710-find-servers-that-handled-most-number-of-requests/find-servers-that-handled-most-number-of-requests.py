class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free = list(range(k))
        heapq.heapify(free)

        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            start = arrival[i]
            end = start + load[i]

            # Release servers that have finished
            while busy and busy[0][0] <= start:
                finish, server = heapq.heappop(busy)

                idx = i + (server - i) % k
                heapq.heappush(free, idx)

            # Drop request if all servers are busy
            if not free:
                continue

            # Select the next available server
            server = heapq.heappop(free) % k

            count[server] += 1

            heapq.heappush(busy, (end, server))

        max_count = max(count)

        return [
            i for i in range(k)
            if count[i] == max_count
        ]
