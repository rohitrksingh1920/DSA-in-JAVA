class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def calc(start1, dur1, start2, dur2):
            minEnd = min(s + d for s, d in zip(start1, dur1))

            return min(
                max(minEnd, s) + d
                for s, d in zip(start2, dur2)
            )

        landThenWater = calc(
            landStartTime, landDuration,
            waterStartTime, waterDuration
        )

        waterThenLand = calc(
            waterStartTime, waterDuration,
            landStartTime, landDuration
        )

        return min(landThenWater, waterThenLand)