class Solution:

    def toSigned11(self, n):
        n = n & 0b11111111111
        return n | (-(n & 0b10000000000))

    def getSum(self, a: int, b: int) -> int:

        carry = 0
        ans = 0

        for i in range(11):

            x = a & 1
            y = b & 1
            a >>= 1
            b >>= 1

            if carry:
                if x and y:
                    res = 1
                    carry = 1
                elif x or y:
                    res = 0
                    carry = 1
                else:
                    res = 1
                    carry = 0
            else:
                if x and y:
                    res = 0
                    carry = 1
                elif x or y:
                    res = 1
                    carry = 0
                else:
                    res = 0
                    carry = 0

            ans |= (res << i)

        return self.toSigned11(ans)

if __name__ == "__main__":

    solution = Solution()

    a = 1
    b = 2

    resp = solution.getSum(a, b)

    print(resp)

