class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        # Minimum price of any item
        minPrice = min(price for factor, price in items)

        # DP: maximum items obtainable using exact budget
        dp = [0] * (budget + 1)

        for factor, price in items:

            # Count items whose factors are divisible by current factor
            count = 0

            for otherFactor, _ in items:
                if otherFactor % factor == 0:
                    count += 1

            # 0/1 Knapsack: first purchase of this item type
            for j in range(budget, price - 1, -1):
                dp[j] = max(dp[j], dp[j - price] + count)

        # Use remaining budget to buy cheapest items
        ans = 0

        for spent in range(budget + 1):
            extra = (budget - spent) // minPrice
            ans = max(ans, dp[spent] + extra)

        return ans
