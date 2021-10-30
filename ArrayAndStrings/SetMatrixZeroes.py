from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        R = len(matrix)
        C = len(matrix[0])

        # iterate to find column indicators
        for i in range(R):
            if matrix[i][0] == 0:
                is_col = True

            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # setting to zeros for inner matrix
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # setting top row.
        if matrix[0][0] == 0:
            for j in range(1, C):
                matrix[0][j] = 0

        # setting first col
        if is_col:
            for i in range(R):
                matrix[i][0] = 0


if __name__ == '__main__':
    sol = Solution()

    matrix = [[0, 1, 2, 0],
              [3, 4, 5, 2],
              [1, 3, 1, 5]]

    sol.setZeroes(matrix)

    print(matrix)
