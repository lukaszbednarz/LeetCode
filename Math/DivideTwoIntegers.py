class Solution:

    # def divide_pos(self, dividend: int, divisor: int) -> int:
    #
    #     if dividend < divisor:
    #         return 0;
    #
    #     ans = 0
    #
    #     while total < dividend:
    #         ans += 1 + self.divide_pos()

    def clip(self, x):
        max_int = (1 << 31) - 1
        min_int = (-1 << 31)

        if x < min_int:
            return min_int
        elif x > max_int:
            return max_int
        else:
            return x


    def divide(self, dividend: int, divisor: int) -> int:

        if divisor == 1:
            return dividend
        elif divisor == -1:
            return self.clip(-dividend)
        elif dividend == 0:
            return dividend

        # same sign
        if ((1 << 32) & dividend) != ((1 << 32) & divisor):

            positive = False

        else:
            positive = True

        dividend = abs(dividend)
        divisor = abs(divisor)

        # store for accumulation so far
        total = 0
        # final answer
        ans = 0

        # store for backtracking
        steps = []

        while (total < dividend) & ((dividend - total) >= divisor):

            if len(steps) == 0:
                total += divisor
                ans += 1
                steps.append((1, divisor))

            elif total < (dividend - total):

                steps.append((ans, total))

                total += total
                ans += ans

            else:

                step = steps.pop()

                while (len(steps) > 0) and step[1] > (dividend - total):
                    step = steps.pop()

                total += step[1]
                ans += step[0]

        if positive:
            return self.clip(ans)
        else:
            return self.clip(-ans)








