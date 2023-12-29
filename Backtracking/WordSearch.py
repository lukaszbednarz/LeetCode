from collections import Counter
from typing import List


class Solution:

    def print_word(self, board, seen):
        print("".join([board[i][j] for (i, j) in seen]))

    def exist(self, board: List[List[str]], word: str) -> bool:

        n = len(board)
        m = len(board[0])

        seen = []

        steps = [(-1, 0),
                 (0, -1),
                 (0, 1),
                 (1, 0)]



        word_counter = Counter(word)
        board_counter = Counter()
        for r in board:
            board_counter.update(r)

        for k, v in word_counter.items():
            if board_counter.get(k, 0) < v:
                return False

        def backtrack(word: str, x, y):

            print(seen)
            self.print_word(board, seen)

            if len(word) == 0:
                return True

            for dx, dy in steps:
                k = x + dx
                l = y + dy

                if (k, l) in seen:
                    continue
                if k < 0 or k >= n:
                    continue
                if l < 0 or l >= m:
                    continue

                if board[k][l] == word[0]:
                    seen.append((k, l))
                    if backtrack(word[1:], k, l):
                        return True
                    _ = seen.pop()
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] != word[0]:
                    continue

                seen.append((i, j))
                if backtrack(word[1:], i, j):
                    return True
                _ = seen.pop()

        return False


if __name__ == "__main__":

    solution = Solution()

    board = [["A", "A", "A", "A", "A", "A"],
             ["A", "A", "A", "A", "A", "A"],
             ["A", "A", "A", "A", "A", "A"],
             ["A", "A", "A", "A", "A", "A"],
             ["A", "A", "A", "A", "A", "A"],
             ["A", "A", "A", "A", "A", "A"]]
    word = "AAAAAAAAAAAAAAa"

    # board = [["A","B","C","E"],
    #          ["S","F","C","S"],
    #          ["A","D","E","E"]]
    # word = "ABCCED"


    resp = solution.exist(board, word)

    print(resp)