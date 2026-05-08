class Solution:
    def buildSieve(self, maxEl):

        self.isPrime = [True] * (maxEl + 1)

        if maxEl >= 0:
            self.isPrime[0] = False

        if maxEl >= 1:
            self.isPrime[1] = False

        num = 2

        while num * num <= maxEl:

            if self.isPrime[num]:

                multiple = num * num

                while multiple <= maxEl:

                    self.isPrime[multiple] = False
                    multiple += num

            num += 1
    def minJumps(self, nums: List[int]) -> int:

        n = len(nums)

        mp = defaultdict(list)
        maxEl = 0

        for i in range(n):

            mp[nums[i]].append(i)
            maxEl = max(maxEl, nums[i])

        self.buildSieve(maxEl)

        queue = deque([0])

        visited = [False] * n
        visited[0] = True

        seen = set()

        steps = 0

        while queue:

            size = len(queue)

            for _ in range(size):

                i = queue.popleft()

                if i == n - 1:
                    return steps

                # i - 1
                if i - 1 >= 0 and not visited[i - 1]:

                    queue.append(i - 1)
                    visited[i - 1] = True

                # i + 1
                if i + 1 < n and not visited[i + 1]:

                    queue.append(i + 1)
                    visited[i + 1] = True

                # skip if not prime or already processed
                if (not self.isPrime[nums[i]]) or (nums[i] in seen):
                    continue

                # visit all multiples
                multiple = nums[i]

                while multiple <= maxEl:

                    if multiple in mp:

                        for j in mp[multiple]:

                            if not visited[j]:

                                queue.append(j)
                                visited[j] = True

                    multiple += nums[i]

                seen.add(nums[i])

            steps += 1

        return -1