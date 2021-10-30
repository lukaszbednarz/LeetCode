import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort(reverse=True)

        if amount == 0:
            return 0

        dp = [-1 for a in range(amount)]

        for i in range(1, amount + 1):

            for c in coins:
                rem = i % c
                count = i // c
                if c > i:
                    continue
                if rem == 0:
                    dp[i - 1] = count
                    break
                elif dp[rem - 1] > 0:
                    dp[i - 1] = count + dp[rem - 1]
                    break

        return dp[amount - 1]

    def coinChange2(self, coins: List[int], amount: int) -> int:

        coins.sort(reverse=True)

        if amount == 0:
            return 0

        _MAX_INT_ = sys.maxsize

        dp = [_MAX_INT_ for a in range(amount + 1 )]
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != _MAX_INT_ else -1



if __name__ == '__main__':
    sol = Solution()

    coins = [186, 419, 83, 408]

    amount = 6250

    output = sol.coinChange2(coins, amount)

    print(output)
