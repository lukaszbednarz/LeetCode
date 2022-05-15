

class Solution:

    def __init__(self):
        self.seen = set()

    def sumOfSquares(self, n: int) -> int:

        sos = 0

        for d in [int(d) ** 2 for d in str(n)]:
            sos += d

        return sos

    def isHappy(self, n: int) -> bool:

        i = 0

        if n == 1:
            return True
        if n in self.seen:
            return False

        while (n != 1) & (n not in self.seen):

            self.seen.add(n)

            n = self.sumOfSquares(n)


        return n == 1
