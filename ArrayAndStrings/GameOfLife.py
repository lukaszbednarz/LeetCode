from collections import deque
from typing import List

_NEIGHBOURS_ = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1]
]


class Solution:

    # def nextState(self, board: List[List[int]], i: int, j: int) -> int:
    #     R = len(board)
    #     C = len(board[0])
    #     count = 0
    #
    #     def isAlive(i: int, j: int) -> bool:
    #         if i < 0 or j < 0 or i >= R or j >= C:
    #             return False
    #         return board[i][j] == 1
    #
    #     for nb in _NEIGHBOURS_:
    #         if count < 4 & isAlive(i + nb[0], j + nb[1]):
    #             count += 1
    #
    #     alive = isAlive(i, j)
    #
    #     if alive:
    #         if count < 2:
    #             return 0
    #         if count < 4:
    #             return 1
    #         return 0
    #
    #     if count == 3:
    #         return 1
    #     return 0

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q = deque()

        R = len(board)
        C = len(board[0])

        def isAlive(i: int, j: int) -> bool:
            if i < 0 or j < 0 or i >= R or j >= C:
                return False
            return board[i][j] == 1

        def nextState(i: int, j: int) -> int:

            count = 0

            for nb in _NEIGHBOURS_:
                if count < 4 & isAlive(i + nb[0], j + nb[1]):
                    count += 1

            alive = isAlive(i, j)

            if alive:
                if count < 2:
                    return 0
                if count < 4:
                    return 1
                return 0

            if count == 3:
                return 1
            return 0

        for i in range(R):
            for j in range(C):
                new_state = nextState(i, j)
                if isAlive(i, j) != new_state:
                    q.append([i, j, new_state])

        while q:
            i, j, state = q.popleft()
            board[i, j] = state


if __name__ == '__main__':
    sol = Solution()

    board = [[0, 1, 0],
             [0, 0, 1],
             [1, 1, 1],
             [0, 0, 0]]

    sol.setZeroes(board)

    print(board)
