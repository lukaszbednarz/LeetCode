# Definition for singly-linked list.
import sys
import threading
from collections import deque
from functools import lru_cache
from typing import Optional, List

import numpy as np

_MOVES_ = [
    (1, 2),
    (1, -2),
    (2, 1),
    (2, -1),
    (-1, 2),
    (-1, -2),
    (-2, 1),
    (-2, -1)
]

class Solution:

    def _buildMatrix(self, n: int) -> np.matrix:
        n2 = n*n
        mat = np.zeros((n2, n2))
        p = 1/8
        for i in range(n*n):
            x = i % n
            y = i // n
            for m in _MOVES_:
                xd = x + m[0]
                yd = y + m[1]

                if xd >= 0 and xd < n and yd >= 0 and yd < n:
                    a = xd + n * yd
                    mat[i, a] = p
                    mat[a, i] = p

        return mat

    def _matpow(self, mat, n):
        return np.linalg.matrix_power(mat, n)


    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        mat = self._buildMatrix(n)
        mat = self._matpow(mat, k)

        state = np.zeros((n*n, 1))
        state[row + n * column] = 1

        ans = np.matmul(mat, state)

        return sum(ans)[0]






if __name__ == '__main__':
    sol = Solution()

    n = 3
    k = 1
    row = 0
    column = 0

    mat = sol._buildMatrix(n)

    print(mat)

    ans = sol.knightProbability(n, k, row, column)

    print(ans)