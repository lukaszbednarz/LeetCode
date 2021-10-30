from functools import lru_cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:



        @lru_cache
        def dp(i, j):
            if i >= m or j >= n:
                return 0

            dx = m - 1 - i
            dy = n - 1 - j

            if dx == 0 or dy == 0:
                return 1

            return dp(i + 1, j) + dp(i, j + 1)

        return dp(0, 0)





if __name__ == '__main__':

    sol = Solution()

    output = sol.uniquePaths(7, 3)

    print(output)
