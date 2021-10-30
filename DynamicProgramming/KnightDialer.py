# Definition for singly-linked list.
import sys
import threading
from collections import deque
from functools import lru_cache
from typing import Optional, List
class Solution:

    def knightDialer3(self, n: int) -> int:
        # equivalence: 0: 1 = 3 = 7 = 9, 1: 2 = 8, 2: 4 = 6, 3: 0, 5
        def matmul(a, b):
            m = len(a)
            n = len(b)
            p = len(b[0])
            res = [[0] * p for _ in range(m)]

            for i in range(m):
                for k in range(n):
                    for j in range(p):
                        res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % LARGE_PRIME
            return res

        def matpow(a, n):
            cur = a

            res = [[0] * len(a) for _ in range(len(a))]
            for i in range(len(a)):
                res[i][i] = 1

            while n > 0:
                if n % 2:
                    res = matmul(res, cur)
                cur = matmul(cur, cur)
                n //= 2

            return res

        if n == 1:
            return 10

        LARGE_PRIME = 10 ** 9 + 7

        d2 = [[2], [2], [3], [2]]
        T = [[0, 1, 1, 0],
             [2, 0, 0, 0],
             [2, 0, 0, 1],
             [0, 0, 2, 0]]

        Tn = matpow(T, n - 2)
        res = matmul(Tn, d2)
        return (4 * res[0][0] + 2 * res[1][0] + 2 * res[2][0] + res[3][0]) % LARGE_PRIME



    def knightDialer2(self, n: int) -> int:
        # paths represents every key we can go to from given key
        # -1 is starting condition, we can start from any key
        paths = {-1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0: [4, 6], 1: [6, 8], 2: [7, 9],
                 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}

        @lru_cache(None)
        def recurse(steps, curr):
            if steps == 0:
                return 1

            count = 0
            for num in paths[curr]:
                count += recurse(steps - 1, num)

            return count

        return recurse(n, -1) % (10 ** 9 + 7)
    # possible transitions considering knight's moves

    def knightDialer(self, n: int) -> int:

        trans = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        @lru_cache
        def numbers(d: int, ni: int):

            if 0 == ni:
                return 0

            if ni == 1:
                return 1

            # if (d, ni) in mem:
            #     return mem[(d, ni)]

            ans = 0
            for t in trans[d]:
                ans += numbers(t, ni - 1)

            # mem[(d, ni)] = ans

            return ans

        ans = 0
        for k in trans:
            ans += numbers(k, n)

        return ans % (10 ** 9 + 7)


if __name__ == '__main__':
    sol = Solution()

    sys.setrecursionlimit(10000)
    output = sol.knightDialer(1000)

    print(output)

    output = sol.knightDialer2(1000)

    print(output)

    output = sol.knightDialer3(1000)

    print(output)
