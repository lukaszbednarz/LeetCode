from typing import List


class Solution:
    seen = set()

    def explore(self, grid: List[List[str]], i: int, j: int) -> None:
        n = len(grid)
        m = len(grid[0])

        steps = [
                # (-1, -1),
                 (-1, 0),
                 # (-1, 1),
                 (0, -1),
                 (0, 1),
                 # (1, -1),
                 (1, 0),
                 # (1, 1)
        ]

        queue = [(i, j)]

        while len(queue) > 0:
            print(f"points to explore:{queue}")
            x, y = queue.pop()

            for dx, dy in steps:

                k = x + dx
                l = y + dy

                if k < 0 or k >= n:
                    continue
                if l < 0 or l >= m:
                    continue

                if (k, l) in self.seen:
                    continue

                if grid[k][l] == "1":
                    queue.append((k, l))

                self.seen.add((k, l))

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        resp = 0

        i = j = 0

        while i < n:
            j = 0
            while j < m:

                if (i, j) in self.seen:
                    j += 1
                    continue

                if grid[i][j] == "1":
                    print(f"exploring i={i}, j={j}")
                    resp += 1
                    self.seen.add((i, j))
                    print(f"seen: {self.seen}")
                    self.explore(grid, i, j)
                    print(f"seen: {self.seen}")
                j += 1

            i += 1

        return resp


if __name__ == "__main__":

    solution = Solution()

    input = [["1","1","0","0","0"],
             ["1","1","0","0","0"],
             ["0","0","1","0","0"],
             ["0","0","0","1","1"]]

    resp = solution.numIslands(input)

    print(resp)