# Definition for singly-linked list.
from collections import deque
from typing import Optional, List

# class Solution:
#     def minKnightMoves(self, x: int, y: int) -> int:
#         x, y = abs(x), abs(y)
#         if (x < y): x, y = y, x
#         if (x == 1 and y == 0): return 3
#         if (x == 2 and y == 2): return 4
#         delta = x - y
#         if (y > delta):
#             return delta - 2 * ((delta - y) // 3);
#         else:
#             return delta - 2 * ((delta - y) // 4);
# https://medium.com/@adematalay/knights-move-on-infinite-chess-board-with-constant-time-and-space-98c1c0748aa6

class Solution:

    _moves=[
        (1, 2),
        (1, -2),
        (2, 1),
        (2, -1),
        (-1, 2),
        (-1, -2),
        (-2, 1),
        (-2, -1)
    ]



    def bfs(self, q, v1, v2) -> int:

        x1, y1, step1 = q.popleft()
        pos = (x1, y1)

        if pos in v1:
            return -1

        else:
            v1[pos] = step1

        if pos in v2:
            return step1 + v2[pos]

        for dx, dy in self._moves:
            q.append((x1 + dx, y1 + dy, step1 + 1))

        return -1





    def minKnightMoves(self, x: int, y: int) -> int:

        v1 = {}
        v2 = {}
        q1 = deque([(0, 0, 0)])
        q2 = deque([(x, y, 0)])

        while q1 and q2:
            steps = self.bfs(q1, v1, v2)

            if steps >= 0:
                return steps

            steps = self.bfs(q2, v2, v1)

            if steps >= 0:
                return steps


if __name__ == '__main__':
    sol = Solution()

    output = sol.minKnightMoves(5, 5)

    print([e for e in output])
