class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:

        # left = [0] * len(robots)
        # right = [0] * len(robots)
        # num = [0] * len(robots)
        # robotsToDistance = {}

        # for i in range(len(robots)):
        #     robotsToDistance[robots[i]] = distance[i]

        # robots.sort()
        # walls.sort()

        # for i in range(len(robots)):
        #     pos1 = bisect.bisect_right(walls, robots[i])

        #     if i >= 1:
        #         leftBound = max(
        #             robots[i] - robotsToDistance[robots[i]], robots[i - 1] + 1
        #         )
        #         leftPos = bisect.bisect_left(walls, leftBound)
        #     else:
        #         leftPos = bisect.bisect_right(
        #             walls, robots[i] - robotsToDistance[robots[i]]
        #         )

        #     left[i] = pos1 - leftPos

        #     if i < len(robots) - 1:
        #         rightBound = min(
        #             robots[i] + robotsToDistance[robots[i]], robots[i + 1] - 1
        #         )
        #         rightPos = bisect.bisect_right(walls, rightBound)
        #     else:
        #         rightPos = bisect.bisect_left(
        #             walls, robots[i] + robotsToDistance[robots[i]]
        #         )

        #     pos2 = bisect.bisect_left(walls, robots[i])
        #     right[i] = rightPos - pos2

        #     if i == 0:
        #         continue

        #     pos3 = bisect.bisect_left(walls, robots[i - 1])
        #     num[i] = pos1 - pos3

        # subLeft, subRight = left[0], right[0]
        # for i in range(1, len(robots)):
        #     currentLeft = max(
        #         subLeft + left[i],
        #         subRight - right[i - 1] + min(left[i] + right[i - 1], num[i]),
        #     )
        #     currentRight = max(subLeft + right[i], subRight + right[i])
        #     subLeft, subRight = currentLeft, currentRight

        # return max(subLeft, subRight)

        left = [0] * len(robots)
        right = [0] * len(robots)
        num = [0] * len(robots)
        robotsToDistance = {}

        for i in range(len(robots)):
            robotsToDistance[robots[i]] = distance[i]

        robots.sort()
        walls.sort()

        for i in range(len(robots)):
            pos1 = bisect.bisect_right(walls, robots[i])

            if i >= 1:
                left_bound = max(
                    robots[i] - robotsToDistance[robots[i]], robots[i - 1] + 1
                )
                left_pos = bisect.bisect_left(walls, left_bound)
            else:
                left_pos = bisect.bisect_left(
                    walls, robots[i] - robotsToDistance[robots[i]]
                )

            left[i] = pos1 - left_pos

            if i < len(robots) - 1:
                right_bound = min(
                    robots[i] + robotsToDistance[robots[i]], robots[i + 1] - 1
                )
                right_pos = bisect.bisect_right(walls, right_bound)
            else:
                right_pos = bisect.bisect_right(
                    walls, robots[i] + robotsToDistance[robots[i]]
                )

            pos2 = bisect.bisect_left(walls, robots[i])
            right[i] = right_pos - pos2

            if i == 0:
                continue

            pos3 = bisect.bisect_left(walls, robots[i - 1])
            num[i] = pos1 - pos3

        sub_left, sub_right = left[0], right[0]
        for i in range(1, len(robots)):
            current_left = max(
                sub_left + left[i],
                sub_right - right[i - 1] + min(left[i] + right[i - 1], num[i]),
            )
            current_right = max(sub_left + right[i], sub_right + right[i])
            sub_left, sub_right = current_left, current_right

        return max(sub_left, sub_right)